from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def listar_producto(request):
    productos = Producto.objects.using('default').all().order_by('id')
    return render(request, 'listar_productos.html', {'productos':productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_producto'))
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html', {'producto_form':form}) 
    
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Datos inválidos para editar el producto')
            return HttpResponseRedirect(reverse('editar_producto', args=[producto.id]))
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'producto_form':form, 'producto_id': producto_id})
    
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('listar_producto')

def index(request):
    return render(request, 'index.html')

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        try:
            query_id = int(query)
        except ValueError:
            query_id = None
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) | 
            (Q(id=query_id) if query_id is not None else Q())
            ).order_by('id')
        return render(request, 'listar_productos.html', {'productos':productos})
    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('listar_producto')
        else:
            messages.error(request, 'Usuario o password inválidos')
            form = AuthenticationForm()
            return render(request, 'login.html', {'form':form}) 
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def registro(request):   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro éxitoso')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Datos inválidos')
            form = UserCreationForm()
            return render(request, 'registro.html', {'form':form}) 
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form':form})
    