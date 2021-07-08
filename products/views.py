import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from datetime       import datetime
from .models        import Product, ProductEfficacy, ProductSummary

class ProductsView(View):
    def get(self, request ):
        try: 
            eye    = request.GET.get('eye','')
            energy = request.GET.get('energy','')
            blood  = request.GET.get('blood','')
            skin   = request.GET.get('skin','')
            
            q_object = Q()

            if eye == 'eye':                 
                eye = Q(productefficacy__name='눈')
                q_object.add(eye,Q.OR)
            if energy=='energy':
                energy = Q(productefficacy__name='활력')
                q_object.add(energy,Q.OR)
            if blood=='blood':
                blood = Q(productefficacy__name='혈액순환')
                q_object.add(blood,Q.OR)            
            if skin=='skin':
                skin = Q(productefficacy__name='피부')
                q_object.add(skin,Q.OR)
            
            products= Product.objects.filter(q_object).distinct()

            results = [
                {
                    "products" : [
                        {
                            "productID"          : product.id,
                            "productName"        : product.name,
                            "productPrice"       : product.price,
                            "productTablet"      : product.tablet,
                            "thumbnail_image_url": product.thumbnail_image_url,
                            "icon_image_url"     : [product_icon.icon for product_icon in Product.objects.get(id=product.id).productefficacy_set.all()],
                            "summary"          : [text.summary for text in Product.objects.get(id=product.id).productsummary_set.all()]
                        }for product in products
                    ] 
                }
            ]
            return JsonResponse({"message":results},status=200)

        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)


class ProductsDetailsView(View): 
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            results = [
                {
                    "productName"        : product.name,
                    "productPrice"       : product.price,
                    "productTablet"      : product.tablet,
                    "thumbnail_image_url": product.thumbnail_image_url,
                    "productDescription" : product.description,
                    "icon_image_url"     : [product_icon.icon for product_icon in product.productefficacy_set.all()],
                    "icon_name"          : [product_icon.name for product_icon in product.productefficacy_set.all()],
                }
            ]
            return JsonResponse({"message":results},status=200)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"},status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)