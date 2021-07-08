from django.urls    import path
from products.views import ProductsView, ProductsDetailsView

urlpatterns = [
    path('/product', ProductsView.as_view()),
    # path('/product', ProductsSelectsView.as_view()),
    path('/product/<int:product_id>', ProductsDetailsView.as_view()),
]