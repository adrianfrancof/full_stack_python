from django.urls import path
from . import views
from .views import IndexPageView, lista_libros

urlpatterns = [
    path('', IndexPageView.as_view(), name="index"),
    path('lista_libros/', lista_libros, name='lista_libros')
]