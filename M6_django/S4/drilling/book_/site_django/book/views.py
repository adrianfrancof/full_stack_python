from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request): # un view o controlador mediant una función
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')

class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'