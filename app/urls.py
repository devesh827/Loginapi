from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib import admin
from django.urls import path,include
from app.views import UserViewSet
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'users',UserViewSet)



urlpatterns = [
    path('logindone/',views.logindone,name='logindone'),
    path('', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('api/',include(router.urls))
]
