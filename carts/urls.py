from django.urls    import path
from carts.views import CartView, CartDeleteView

urlpatterns = [
    path('', CartView.as_view()),
    path('/<int:product_id>', CartDeleteView.as_view()),
]