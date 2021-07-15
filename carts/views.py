import json
import bcrypt
import jwt
from datetime import datetime

from django.http            import JsonResponse
from django.views           import View
from django.db.models       import Q
from django.core.exceptions import ObjectDoesNotExist


from core.models       import TimeStampModel
from core.views        import check_login
from my_settings       import SECRET_KEY, ALGORITHM
from users.models      import User, Point
from products.models   import Product, ProductEfficacy, ProductSummary, Efficacy
from .models           import Cart

class CartView(View):
    @check_login
    def post(self, request):
        try:             
            data                    = json.loads(request.body)
            user                    = request.user
            product                 = Product.objects.get(id=data['productID'])
            cart_object, cart_exist = Cart.objects.get_or_create(user_id=user.id, product_id=product.id)

            if not cart_exist:
                return JsonResponse({"message":f'{product.id}_IS_ALREADY_EXISTS'},status=400)
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
            
        except ObjectDoesNotExist:
            return JsonResponse({'message' : 'MODEL_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)


    @check_login
    def get(self, request):
        try: 
            user  = request.user
            carts = Cart.objects.filter(user_id=user.id)
            results = [{
                "productID"        : cart.product.id,
                "productName"        : cart.product.name,
                "quantity"           : cart.quantity, 
                "productPrice"       : int(cart.product.price),
                "thumbnail_image_url": cart.product.thumbnail_image_url,
            }for cart in carts]

            point = Point.objects.get(user=user).point
            return JsonResponse({"product":results,"point":point},status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'message' : 'MODEL_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)

    @check_login
    def patch(self, request):
        try: 
            data = json.loads(request.body)
            user = request.user
            Cart.objects.filter(product_id=data["productID"], user=user).update(quantity = data["quantity"])
            return JsonResponse({"message":"UPDATE_COMPLETED"},status=200) 
            
        except ObjectDoesNotExist:
            return JsonResponse({'message' : 'MODEL_ERROR'}, status=400)
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)

    @check_login
    def delete(self, request):
        try: 
            item = request.GET.getlist('item',None)
            q_object = Q()
            if item: 
                q_object &= Q(product_id__in= item)
            
            Cart.objects.filter(q_object).delete()
            
            return JsonResponse({"message":"DELETE_COMPLETED"},status=204)
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message' : 'MODEL_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)