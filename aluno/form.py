from django.forms import ModelForm
from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
        labels = {
            'data_nasc': 'Data de nascimento',
            'telefone2': 'Telefone Emergencial',
            'cpf': 'CPF',
            'rg': 'RG',
            'email': 'E-mail',
            'telefone2': 'Telefone Emergencial',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'numero': 'Número',
            'uf': 'UF',
            'matricula': 'Matrícula',
            'serie': 'Série/ano',
            'observacoes': 'Observações',


        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "data_nasc": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "sexo": forms.Select(attrs={"class": "form-select"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "rg": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "telefone2": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "endereco": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "complemento": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "uf": forms.Select(attrs={"class": "form-select"}),
            "matricula": forms.TextInput(attrs={"class": "form-control"}),
            "curso": forms.Select(attrs={"class": "form-select"}),
            "serie": forms.Select(attrs={"class": "form-select"}),
            "turno": forms.Select(attrs={"class": "form-select"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
