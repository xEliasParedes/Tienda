#from django.conf.urls import urls
from django.urls import path
from . import views



urlpatterns = [
    path ('login/',views.login, name='login'),
    path ('signup/',views.registro, name='registro'),
]