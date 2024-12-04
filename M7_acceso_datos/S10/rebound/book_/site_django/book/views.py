from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
def index(request): # un view o controlador mediant una función
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')

class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'
    
def palindromo(request, palabra): # yo hago yoga hoy
    es_palindromo = ''
    
    palabra_sin_espacios = palabra.replace(' ', '')   #yohagoyogahoy
    if palabra_sin_espacios == palabra_sin_espacios[::-1] :
        es_palindromo = 'ES PALINDROMO'
    else: # si no lo es
        es_palindromo = 'NO ES PALINDROMO'
    
    context = {'es_palindromo': es_palindromo, 'palabra': palabra}
    return render(request,'espalindromo.html', context)

def palabra(request, user):
    return render(request, 'username.html', {'user':user})