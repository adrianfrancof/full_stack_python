from django.urls import path
from . import views
# importar views
from .views import IndexPageView, lista_libros, crear_libro, editar_libro, eliminar_libro 
from .views import registro, iniciar_sesion, home_page, cerrar_sesion
urlpatterns = [
    # path(ruta, view, name=nombre_de_la_ruta)
    path('', IndexPageView.as_view(), name='index'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('crear_libro/', crear_libro, name='crear_libro'), # registrando ruta para crear libro
    path('editar_libro/<int:libro_id>', editar_libro, name='editar_libro'), # registrando ruta para editar libro
    path('eliminar_libro/<int:libro_id>', eliminar_libro, name='eliminar_libro'), # registrando ruta para eliminar libro
    path('registro/', registro, name='registro'), # registrando ruta para el formulario de registro
    path('login/', iniciar_sesion, name='login'), # registrando ruta para el login
    path('home/', home_page, name='home'), # registrando ruta para la pagina principal
    path('logout/', cerrar_sesion, name='logout') # registrando ruta para cerrar sesion
]