#from django.conf.urls import urls
from django.urls import path
from . import views



urlpatterns = [
    path('', views.list_producto, name='list_product'),
    path('ARCHIVO', views.producto, name='producto')
]