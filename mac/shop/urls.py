
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('',views.Sign_up.as_view(),name='sign_up_page'),
   path('index/',views.index,name='homepage'),
   path('login/',views.Log_in.as_view(),name='log_in_page'),
   path('delete/<int:id>',views.delete_customer,name='delete_customer')
]

