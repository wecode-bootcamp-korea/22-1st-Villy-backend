from django.urls    import path
from products.views import ProductsView

urlpatterns = [
    path('/product', ProductsView.as_view()),
    path('/product/<product_id>', ProductslView.as_view()),
]