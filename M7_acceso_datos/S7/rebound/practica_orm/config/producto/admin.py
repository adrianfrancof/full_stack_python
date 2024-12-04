from django.contrib import admin
from .models import Fabrica, Producto

# Register your models here.
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'pais')
    list_display_links = ['nombre', 'pais']
    list_filter = ('nombre', 'pais')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_vencimiento', 'precio', 'fabrica')
    list_display_links = ['id', 'nombre']
    list_filter = ('nombre', 'fabrica')   
    
admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)