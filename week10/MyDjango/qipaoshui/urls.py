from django.urls import path
from . import views
urlpatterns = [

    path('', views.estimate_url),
    path('<str:login>', views.login_url),
    # path('<int:>',views.index_url),
]