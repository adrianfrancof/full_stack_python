from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'
    
def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

# https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/
# https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
def crear_libro(request):
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST)
        if form.is_valid(): # si el formulario es validofrom django.contrib import messages
            form.save() # guarda los datos en la base de datos
            messages.success(request, 'Libro creado correctamente') # muestra un mensaje https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            return redirect('lista_libros') # redirecciona a lista_libros
        else: # si el formulario no es valido
            messages.error(request, 'Módifica los datos de ingreso') # muestra un mensaje
            return HttpResponseRedirect(reverse('crear_libro')) # redirecciona a la pagina
    else: # si el metodo es GET
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})
    
def editar_libro(request, libro_id):
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la db o status 404 not found
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) # instancia del formulario con los datos del libro a editar
        if form.is_valid(): # si el formulario es valido
            form.save() # guarda los datos en la base de datos
            return redirect('lista_libros') # redirecciona a lista de libros
        else:  # si el formulario no es valido
            messages.error(request, 'Módifica los datos de ingreso') # muestra un mensaje
            return HttpResponseRedirect(reverse('editar_libro', args=[book.id])) # redirecciona a la pagina
    else: # si el metodo es GET
        form = BookForm(instance=book) # instancia del formulario con los datos del libro a editar
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id}) # renderiza la vista para editar el libro
    
def eliminar_libro(request, libro_id):
    book = get_object_or_404(Book, pk=libro_id) # obteniendo el libro a eliminar en la db o status 404 not found
    book.delete() # eliminando el libro de la base de datos
    messages.success(request, 'Libro eliminado correctamente') # muestra un mensaje
    return redirect('lista_libros')  # redirecciona a lista de libros