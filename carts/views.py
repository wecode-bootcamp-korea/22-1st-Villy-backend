import json
from datetime       import datetime

from django.http    import JsonResponse
from django.views   import View

from productsmodels        import Product, ProductEfficacy, ProductSummary, 
from .models        import Cart

class ProductsView(View):
    def get(self, request):
        try: 
            eye = request.GET.get('eye','')
            energy = request.GET.get('energy','')
            blood = request.GET.get('blood','')
            skin = request.GET.get('skin','')
            
            products = Product.objects.all()