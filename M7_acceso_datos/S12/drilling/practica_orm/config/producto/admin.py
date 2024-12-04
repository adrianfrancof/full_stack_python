from django.contrib import admin
from .models import Fabrica, Producto

# Register your models here.
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'pais')
    list_display_links = ['nombre', 'pais']
    list_filter = ('nombre', 'pais')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_vencimiento', 'precio', 'fabrica_nombre')
    list_display_links = ['id', 'nombre']
    list_filter = ('nombre', 'fabrica')
    
    def fabrica_nombre(self, obj):
        return obj.fabrica.nombre if obj.fabrica else '-'
    fabrica_nombre.short_description = 'Fábrica'

    
admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)