from django.urls import path

from users.views import SignupView, SignInView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/signin', SignInView.as_view())
]