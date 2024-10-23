from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Book

# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'
    
def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})