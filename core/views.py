import jwt

from django.http import JsonResponse

from my_settings  import SECRET_KEY, ALGORITHM
from users.models import User 

def check_login(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            payload      = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user         = User.objects.get(id = payload['id'])
            request.user = user
    
            return func(self, request, *args, **kwargs)
        
        except jwt.DecodeError:
            return JsonResponse({'message': 'INVAILD_USER'}, status=400)

    return wrapper