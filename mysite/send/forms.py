from django import forms
from .models import Client
from django.forms import TextInput



class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('Nom', 'oficina', 'correu', 'missatge',)
