from django.urls import path
from .views import listar, crear, editar, eliminar_producto, index, buscar, login_user, logout_user, registro

urlpatterns = [
    # home
    path('', index, name='index'),
    # producto
    path('listar_producto/', listar, name='listar_producto'),
    path('crear_producto/', crear, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('buscar/', buscar, name='buscar'),
    # autenticación
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('registro/', registro, name='registro')
]