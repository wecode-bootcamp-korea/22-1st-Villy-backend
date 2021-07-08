from django.urls    import path
from products.views import ProductsView, ProductsDetailsView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('/<int:product_id>', ProductsDetailsView.as_view()),
]