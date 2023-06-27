#from django.conf.urls import urls
from django.urls import path
from . import views



urlpatterns = [
    path('listado_producto/', views.list_producto, name='list_product'),
    path('producto/', views.producto, name='producto')
]