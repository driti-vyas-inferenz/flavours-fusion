from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegisterView, Login, LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
