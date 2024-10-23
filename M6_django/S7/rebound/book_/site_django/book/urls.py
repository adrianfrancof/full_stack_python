from django.urls import path
from . import views
from .views import IndexPageView, lista_libros, crear_libro

urlpatterns = [
    path('', IndexPageView.as_view(), name="index"),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('crear_libro/', crear_libro, name='crear_libro')
]