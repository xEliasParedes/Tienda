#from django.conf.urls import urls
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index')

]