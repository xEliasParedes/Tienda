#from django.conf.urls import urls
from django.urls import path
from . import views



urlpatterns = [
    path('', views.login, name='login'),
    path('registro/', views.registro, name='registro')
]