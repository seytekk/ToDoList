from django.urls import path
from .views import signup, login_user


urlpatterns = [
    path('register/', signup, name="register"),
    path('login/', login_user, name="login")
]