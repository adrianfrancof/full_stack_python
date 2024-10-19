from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')
