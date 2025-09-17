from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'cpf','curso', 'ano', 'turno', 'status')
    fields = ('nome', 'data_nasc', 'cpf', 'rg', 'sexo' , 'email', 'telefone', 'telefone2', 'cep', 'endereço', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'matricula', 'curso', 'ano', 'turno', 'observacoes')
