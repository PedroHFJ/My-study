from django import forms
from .models import Despesas, Receita

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
        windgets = {
            'data' : forms.DateInput(attrs={'type' : 'date'}),
        }
