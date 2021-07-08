import json
from datetime       import datetime

from django.http    import JsonResponse
from django.views   import View

from .models        import Product, ProductEfficacy, ProductSummary

class ProductsView(View):
    def get(self, request):
        try: 
            eye = request.GET.get('eye','')
            energy = request.GET.get('energy','')
            blood = request.GET.get('blood','')
            skin = request.GET.get('skin','')
            
            products = Product.objects.all()

            if eye=='eye': 
                products = Product.objects.filter(productefficacy__name='눈')
            if energy=='energy':
                products = Product.objects.filter(productefficacy__name='활력') 
            if blood=='blood':
                products = Product.objects.filter(productefficacy__name='혈액순환')
            if skin=='skin':
                products = Product.objects.filter(productefficacy__name='피부')

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










# class ProductsView(View):
#     def get(self, request):
#         try: 
#             eye = request.GET.get('eye',None)
#             energy = request.GET.get('energy',None)
#             blood = request.GET.get('blood',None)
#             skin = request.GET.get('skin',None)
            
#             products = Product.objects.all()
            
            
            
#             efficacy_list = [eye,energy,blood,skin]

#             def valid_product(efficacy_list):
#                 valid_list=[]
#                 for x in efficacy_list: 
#                     if x:
#                         valid_list.append(x)
#                 return valid_list
            
#             Product.objects.filter(Q(productefficacy__name='눈') | Q(productefficacy__name='활력'))

            
            
#             if eye: 
#                 products = Product.objects.filter(productefficacy__name='눈')
#             if energy: 
#                 products = Product.objects.filter(productefficacy__name='활력') 
#             if blood: 
#                 products = Product.objects.filter(productefficacy__name='혈액순환')
#             if skin: 
#                 products = Product.objects.filter(productefficacy__name='피부')

#             results = [
#                 {
#                     "products" : [
#                         {
#                             "productID"          : product.id,
#                             "productName"        : product.name,
#                             "productPrice"       : product.price,
#                             "productTablet"      : product.tablet,
#                             "thumbnail_image_url": product.thumbnail_image_url,
#                             "icon_image_url"     : [product_icon.icon for product_icon in Product.objects.get(id=product.id).productefficacy_set.all()],
#                             "summary"          : [text.summary for text in Product.objects.get(id=product.id).productsummary_set.all()]
#                         }
#                     ] for product in products
#                 }
#             ]
#                 return JsonResponse({"message":results},status=200)

#         except TypeError:
#             return JsonResponse({"message":"TYPE_ERROR"},status=400)