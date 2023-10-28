from django.urls import path
from . import views
from app1 import views
urlpatterns = [
path('', views.SignupPage, name='signup'),
path('login/', views.LoginPage, name='login'),
]