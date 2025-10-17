from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):   
    list_display = ( 'nombre_producto', 'precio', 'stock', 'descripcion')