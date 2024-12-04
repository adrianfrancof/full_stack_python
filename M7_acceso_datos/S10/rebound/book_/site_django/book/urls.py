from django.urls import path
from . import views
from .views import IndexPageView, palindromo, palabra

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('', IndexPageView.as_view(),name="index"),
    path('palindromo/<str:palabra>', palindromo, name='palindromo'),
    path('username/<str:user>', palabra)
]