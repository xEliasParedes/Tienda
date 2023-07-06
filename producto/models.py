from django.db import models
from dateutil.relativedelta import relativedelta

# Create your models here.

class producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)          
    cantidad = models.CharField(max_length=3)        
    descripcion = models.CharField(max_length=330)    
    precio_new = models.CharField(max_length=6)
    precio_old = models.CharField(max_length=6)     
    marca =models.ForeignKey('marca',on_delete=models.CASCADE, db_column='id_marca')          
    provedor =models.ForeignKey('provedor', on_delete=models.CASCADE, db_column='id_provedor')     
    despacho = models.BooleanField()    
    retiro =  models.BooleanField() 
    sub_categoria = models.ForeignKey('sub_categoria', on_delete=models.CASCADE, db_column='id_sub_categoria')

    def __str__(self):
        return str(self.nombre)


class marca(models.Model):
    id_marca = models.CharField(primary_key=True, max_length= 2, db_column='id_marca')  
    nombre = models.CharField(max_length=35)
    categoria = models.ForeignKey('categoria', on_delete=models.CASCADE, db_column='id_categoria') 

    def __str__(self):
        return str(self.nombre) 

class provedor(models.Model):
    id_provedor = models.CharField(primary_key=True, max_length=2, db_column='id_provedor')
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return "provedor: "+str(self.nombre)


class despacho(models.Model):
    id_soli_des = models.AutoField(primary_key=True, db_column= 'id_soli_des')
    direccion = models.CharField(max_length=100)  
    num_casa_dep= models.CharField(max_length=3, blank=True, null=True)
    info_add = models.CharField(max_length=100, blank=True, null=True)  
    comuna = models.ForeignKey('comuna', on_delete=models.CASCADE,db_column='id_comuna')
    receptor =  models.CharField(max_length=65)

    def __str__(self):
        return str(self.id_soli_des)+"-"+str(self.direccion)+"-"+str(self.comuna)

class retiro(models.Model):
    id_soli_ret = models.AutoField(primary_key=True,  db_column= 'id_soli_ret')
    fecha_estimada = relativedelta(days=15)
    sucursal= models.ForeignKey('sucursal', on_delete=models.CASCADE, db_column='id_sucursal')
    receptor =  models.CharField(max_length=65)
    
    def __str__(self):
        return str(self.id_soli_ret)+"-"+str(self.sucursal)+"-"+str(self.fecha_estimada)



class sucursal(models.Model):
    id_sucursal = models.CharField(primary_key=True, max_length=4)
    direccion = models.CharField(max_length=100) 
    nombre = models.CharField(max_length=50)
    comuna = models.ForeignKey('comuna', on_delete=models.CASCADE, db_column='id_comuna')

    def __str__(self):
        return str(self.direccion)

class comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True,  db_column='id_comuna')
    nombre = models.CharField(max_length=20)
    region = models.ForeignKey('region', on_delete=models.CASCADE, db_column='id_region')

    def __str__(self):
        return str(self.nombre)+"-"+str(self.region)

class region(models.Model):
    id_region = models.AutoField(primary_key=True,  db_column='id_region')
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, db_column= 'id_categoria')
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)


class sub_categoria(models.Model):
    id_sub_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    categoria = models.ForeignKey('categoria', on_delete=models.CASCADE, db_column='id_categoria')


    def __str__(self):
        return str(self.nombre)+"-"+str(self.categoria)



    

