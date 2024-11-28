from django.urls import path
from .views import listar, crear, editar

urlpatterns = [
    path('listar/', listar, name='listar'),
    path('crear/', crear, name='crear'),
    path('editar/<int:producto_id>', editar, name='editar'),
]