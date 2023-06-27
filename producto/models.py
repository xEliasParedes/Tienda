from django.db import models

# Create your models here.



class producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=43)
    old = models.IntegerField(max_length=6)
    new = models.IntegerField(max_length=6)
    descripcion = models.CharField(max_length=800)
    esContenido = models.CharField(max_length=10)
    esTipoProducto = models.CharField(max_length=20)
    esOrigen = models.CharField(max_length=30)
    esGarantia = models.CharField(max_length=20)
    despacho = models.BooleanField()
    retiro = models.BooleanField()
    
class provedor(models.Model):
    idProvedor = models.IntegerField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=25)


class marca(models.Model):
    idMarca = marca = models.IntegerField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=20)



class envio(models.Model):
    idEnvio = models.IntegerField(primary_key=True, max_length=4)
    direccion = models.CharField(max_length=200)
    comentario = models.CharField(max_length=350)


class region(models.Model):
    idRegion = models.IntegerField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=25)

class comuna(models.Model):
    idRegion = models.IntegerField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=25)
