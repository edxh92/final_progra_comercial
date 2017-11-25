from django import forms
from .models import Menu


class Menu(forms.ModelForm):
    class Meta:
        model=Menu
        fields=('nombre','descripcion','costo_puntada')
