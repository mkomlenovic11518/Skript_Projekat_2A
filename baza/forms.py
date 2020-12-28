from django.forms import ModelForm
from django import forms
from .models import Proizvodjac, Roba
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProizvodjacForm(ModelForm):
    class Meta:
        model=Proizvodjac
        fields=['naziv_proizvodjac','sifra_proizvodjac']

class RobaForm(ModelForm):
    class Meta:
        model=Roba
        fields=['naziv_robe','sifra_robe','kolicina','proizvodjac']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')