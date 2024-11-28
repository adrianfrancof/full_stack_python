from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

# views o controller para página inicial
def index(request):
    return render(request, 'index.html')

# views o controller para listar los vehiculos
def listar(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

# views o controller para crear vehiculo
def crear(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
        else:
            HttpResponseRedirect(reverse('crear'))
    else:
        form = VehiculoForm()
        return render(request, 'crear_vehiculo.html', {'form':form})
            

# views o controller para editar un vehiculo

# views o controller para eliminar un vehiculo

# views o controller para registrar usuario

# views o controller para login

# views o controller para cerrar sesión