from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('home1',about,name='home1'),
    path('index',func,name='index'),
    path('register',regfunc,name='reg_name')
]
