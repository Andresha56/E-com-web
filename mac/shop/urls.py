
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('',views.sign_up,name='homepage'),
   path('index/',views.index,name='homepage'),
   path('login/',views.log_in,name='log_in_page')
]

