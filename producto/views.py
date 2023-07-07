from django.shortcuts import render
from . models import Producto

# Create your views here.
def list_product(request):
    producto= Producto.objects.all()
    context={ 'producto': producto}
    return render(request, 'producto/listado_producto.html', context)

def producto_0(request):
    context={}
    return render(request, 'producto/producto.html', context)