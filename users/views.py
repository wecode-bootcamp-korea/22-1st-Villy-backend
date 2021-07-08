import json
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from users.models import User

class SignInView(View):
    def post(self, request):

        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password'].encode('utf-8')

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            user        = User.objects.get(email=email)
            db_password = user.password.encode('utf-8')

            if not bcrypt.checkpw(password, db_password):
                return JsonResnse({'message' : 'INVALID_PASSWORD'}, status=401)
            
            token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({'token' : token, 'message' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
