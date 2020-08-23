from django.urls import path
from . import views

urlpatterns = [

    path('', views.login2),
    path('login2', views.login2),
    
]
