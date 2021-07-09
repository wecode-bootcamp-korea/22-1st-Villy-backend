import json
from datetime          import datetime

from django.http       import JsonResponse
from django.views      import View

from productsmodels    import Product, ProductEfficacy, ProductSummary, 
from .models           import Cart

def non_user_accept_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try: 
            access_token = request.headers.get('Authorization', None)
            if not access_token: 
                request.user = None 
                return func(self, request, *args, **kwargs)
            payload = jwt.decode(access_token, SECRET, algorithms=ALGORITHM)
            login_user = User.objects.get(id=payload['id'])            
            request.user = login_user
            return func(self, request, *args, **kwargs)
    return wrapper

class ProductsView(View):
    @non_user_accept_decorator
    def post(self, request):
        try: 
            