import bcrypt
import json
import jwt

from django.http  import JsonResponse
from django.views import View

from my_settings import SECRET_KEY, ALGORITHM
from users.models import User
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
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            user = User.objects.create(
                name=data['name'],
                email=data['email'],
                password=hashed_password.decode('utf-8'),
                mobile=data['mobile'],
            )
            access_token = jwt.encode({'id': user.id}, SECRET_KEY, SECRET_ALGORITHM)

            return JsonResponse({'message': 'SUCCESS', 'access_token': access_token}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
