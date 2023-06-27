from django.shortcuts import render

# Create your views here.
def list_producto(request):
    context={}
    return render(request, 'producto/listado_producto.html', context)

def producto(request):
    context={}
    return render(request, 'producto/producto.html', context)