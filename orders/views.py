import json
import bcrypt
import jwt
import uuid
from datetime          import datetime

from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q

from core.models       import TimeStampModel
from core.views        import check_login
from my_settings       import SECRET_KEY, ALGORITHM
from users.models      import User, PointHistory, Point
from products.models   import Product, ProductEfficacy, ProductSummary, Efficacy
from carts.models      import Cart
from .models           import OrderStatus, OrderListStatus, Shipment, Order, OrderItem

class OrderView(View):
    @check_login
    def post(self, request):
        try: 
            data         = json.loads(request.body)
            user         = request.user
            point        = user.point_set.get(id=1).point

            product_dict = data['products']
            id_quantity  = {value["product_id"]:value["quantity"] for (key,value) in product_dict.items()}
            total_price  = 0
            
            for product_id, quantity in id_quantity.items():
                product_price  = Product.objects.get(id=product_id).price
                total_price   += int(quantity)*int(product_price)

            if int(point) >= int(total_price):
                updated_point = int(point) - int(total_price)
                user.point_set.filter(id=1).update(point= updated_point) 
                
                new_uuid = uuid.uuid4()
                Order.objects.create(
                    user_id         = user.id,
                    order_status_id = Order.objects.get(id=1).id,
                    order_number    = new_uuid
                    )          
                
                order = Order.objects.get(order_number=new_uuid)

                PointHistory.objects.create(
                    order = order,
                    point = int(total_price)
                )
                
                for product_id, quantity in id_quantity.items():
                    OrderItem.objects.create(
                        order_id             = order.id,
                        product_id           = Product.objects.get(id=product_id).id,
                        quantity             = quantity,
                        shipment_id          = Shipment.objects.get(id=1).id,
                        order_list_status_id = OrderListStatus.objects.get(id=1).id
                    )
                    Cart.objects.filter(user_id=user.id, product_id=product_id).delete()

                return JsonResponse({'message' : 'SUCCESS'}, status=200)
            return JsonResponse({'message' : 'NOT_ENOUGH_POINTS'}, status=401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)