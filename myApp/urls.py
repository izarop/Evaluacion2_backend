from django.urls import path
from . import views

urlpatterns = [

     path('',views.principal, name="inicio"),
     path('detalle_prod/<int:id>', views.producto_detalle, name='detalle_prod'),
     path('categorias/', views.categorias, name='categorias'),
     path('categorias/<int:id>', views.categoria_detalle, name='categoria_detalle')

    #
 
]
