from django.shortcuts import render
from producto.models import Producto

# Create your views here.
def index(request):
    productos= Producto.objects.all()
    context={'productos':productos}
    return render(request, 'principal/index.html', context)