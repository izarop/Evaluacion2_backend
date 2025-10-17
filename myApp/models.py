from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=350)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre_producto
   
