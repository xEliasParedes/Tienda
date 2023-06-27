from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'principal/index.html', context)

def list_producto(request):
    context={}
    return render(request, 'producto/listado_producto.html', context)
