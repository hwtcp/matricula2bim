from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'serie', 'turno', 'status')
    search_fields = ('nome', 'matricula', 'cpf', 'email')
