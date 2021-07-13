import json
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from my_settings      import SECRET_KEY, ALGORITHM
from users.models     import User, Point
from users.validation import validate_name, validate_email, validate_password, validate_mobile

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not validate_name(data['name']):
                return JsonResponse({'message': 'INVALID_NAME_FORMAT'}, status=401)

            if not validate_email(data['email']):
                return JsonResponse({'message': 'INVALID_EMAIL_FORMAT'}, status=401)

            if not validate_password(data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD_FORMAT'}, status=401)

            if not validate_mobile(data['mobile']):
                return JsonResponse({'message': 'INVALID_MOBILE_FORMAT'}, status=401)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'ALREADY_EXISTED_EMAIL'})
            
            if User.objects.filter(mobile=data['mobile']).exists():
                return JsonResponse({'message': 'ALREADY_EXISTED_NUMBER'})                

            encoded_password = data['password'].encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            user = User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = hashed_password.decode('utf-8'),
                mobile   = data['mobile'],
            )
            
            Point.objects.create(user, point = 1000000)

            access_token = jwt.encode({'id': user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({'message': 'SUCCESS', 'access_token': access_token}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class SigninView(View):
    def post(self, request):

        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password'].encode('utf-8')

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            user            = User.objects.get(email=email)
            hashed_password = user.password.encode('utf-8')

            if not bcrypt.checkpw(password, hashed_password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=401)
            
            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({'message' : 'SUCCESS', 'access_token' : access_token}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)