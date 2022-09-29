from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def pacientes(request):
    pacientes = Paciente.objects.all()
    print(pacientes)
    return render(request, 'libros/index.html', {'paciente': pacientes })    
def crear(request):
    formulario = PacienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request, 'libros/crear.html', {'formulario': formulario})
def editar(request):
    return render(request, 'libros/editar.html')