from django import forms
from .models import Despesas, Receita, PerfilMEI
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesas
        fields = ['descricao', 'categoria', 'valor', 'data', 'tipo']
        widgets = {
            'data' : forms.DateInput(attrs={'type' : 'date'}),
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'quantidade_vendida','data']
        widgets = {
            'data' : forms.DateInput(attrs={'type' : 'date'}),
        }

class CadastroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PerfilMEIForm(forms.ModelForm):
    class Meta:
        model = PerfilMEI
        fields = ['cnpj', 'categoria_MEI']