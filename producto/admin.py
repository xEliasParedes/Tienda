from django.contrib import admin

from .models import comuna , region, envio, marca, provedor, producto

# Register your models here.

admin.site.register(producto)
admin.site.register(provedor)
admin.site.register(marca)
admin.site.register(envio)
admin.site.register(region)
admin.site.register(comuna)