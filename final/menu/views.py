from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import MenuForm
from menu.models import Menu
# Create your views here.

def menu_nuevo(request):
   if request.method == "POST":
      formulario = MenuForm(request.POST)
      if formulario.is_valid():
         menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'],descripcion=formulario.cleaned_data['descripcion'], costo_puntada = formulario.cleaned_data['costo_puntada'])
      return redirect('/')
   else:
       formulario = MenuForm()
   return render(request, 'menu_nuevo.html', {'formulario': formulario})
