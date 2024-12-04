from django.urls import path
from .views import listar, crear, editar, eliminar_producto, index, buscar

urlpatterns = [
    path('', index, name='index'),
    path('listar_producto/', listar, name='listar_producto'),
    path('crear_producto/', crear, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('buscar/', buscar, name='buscar')
]