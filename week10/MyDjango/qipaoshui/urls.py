from django.urls import path
from . import views
urlpatterns = [

    path('', views.estimate_url),
    path('login', views.login_url),
    path('index',views.index_url),
]