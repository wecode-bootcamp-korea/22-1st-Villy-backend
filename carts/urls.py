from django.urls    import path
from carts.views import CartView

urlpatterns = [
    path('', CartView.as_view()),
]