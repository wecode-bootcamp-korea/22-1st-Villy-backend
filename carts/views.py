import json
import bcrypt
import jwt
from datetime          import datetime

from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q

from core.models       import TimeStampModel
from core.views        import check_login
from my_settings       import SECRET_KEY, ALGORITHM
from users.models      import User
from products.models   import Product, ProductEfficacy, ProductSummary, Efficacy
from .models           import Cart


class CartView(View):
    @check_login
    def post(self, request):
        try: 
            data    = json.loads(request.body)
            user    = request.user
            product = Product.objects.get(id=data['productID'])

            Cart.objects.create(user_id=user.id, product_id=product.id)

            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)

    @check_login
    def get(self, request):
        try: 
            user  = request.user
            carts = Cart.objects.filter(user_id=user.id)
            results = [{
                "productName"        : cart.product.name,
                "quantity"           : cart.quantity, 
                "productPrice"       : int(cart.product.price),
                "thumbnail_image_url": cart.product.thumbnail_image_url,
            }for cart in carts]

            return JsonResponse({"message":results},status=200)

        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)

    @check_login
    def patch(self, request):
        try: 
            data    = json.loads(request.body)
            user    = request.user
            product = Product.objects.get(id=data["productID"])
            
            Cart.objects.filter(product_id=product, user_id=user).update(quantity = data["quantity"])

            return JsonResponse({"message":"UPDATE_COMPLETED"},status=200)

        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

    @check_login
    def delete(self, request):
        try: 
            data    = json.loads(request.body)
            user    = request.user
            product = Product.objects.get(id=data["productID"])

            Cart.objects.filter(product_id=product, user_id=user).delete()

            return JsonResponse({"message":"DELETE_COMPLETED"},status=204)
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)