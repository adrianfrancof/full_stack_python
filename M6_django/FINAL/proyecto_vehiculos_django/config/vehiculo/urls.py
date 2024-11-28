from django.urls import path

from .views import index, listar, crear

urlpatterns = [
    path('', index, name='index'),
    path('listar_vehiculo/', listar, name= 'listar'),
    path('crear_vehiculo/', crear, name= 'crear')
]