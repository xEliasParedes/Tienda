from django.shortcuts import render

# Create your views here.
def list_product(request):
    context={}
    return render(request, 'producto/listado_producto.html', context)

def producto_0(request):
    context={}
    return render(request, 'producto/producto.html', context)