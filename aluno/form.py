from django.forms import ModelForm
from django import forms
from .models import Aluno

class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_nasc'  : forms.TextInputInput(attrs={'class': 'form-control' }),
            'cpf' : forms.TextInput(attrs={'class': 'form-control' }),
            'rg' : forms.TextInput(attrs={'class': 'form-control' }),
            'sexo': forms.Select(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'telefone' : forms.TextInput(attrs={'class': 'form-control' }),
            'telefone2' : forms.TextInput(attrs={'class': 'form-control' }),
            'cep' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'complemento' : forms.TextInput(attrs={'class': 'form-control' }),
            'bairro' : forms.TextInput(attrs={'class': 'form-control' }),
            'cidade': forms.TextInput(attrs={'class': 'form-control' }),
            'uf': forms.Select(attrs={'class': 'form-control' }),
            'matricula' : forms.TextInput(attrs={'class': 'form-control' }),
            'curso': forms.Select(attrs={'class': 'form-control' }),
            'ano': forms.Select(attrs={'class': 'form-control' }),
            'turno': forms.Select(attrs={'class': 'form-control' }),
            'obervacoes' : forms.TextInput(attrs={'class': 'form-control' }),

        }