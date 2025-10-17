"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno.views import listar_alunos, aluno_criar, aluno_update, aluno_excluir, aluno_desativar, aluno_detalhes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_alunos, name='listar_alunos'),
    path('aluno/novo/', aluno_criar, name='aluno_criar'),
    path('aluno/<int:pk>/editar/', aluno_update, name='aluno_update'),  
    path('aluno/<int:pk>/excluir/', aluno_excluir, name='aluno_excluir'),
    path('aluno/<int:pk>/desativar/', aluno_desativar, name='aluno_desativar'),
    path('aluno/<int:pk>/detalhes/', aluno_detalhes, name='aluno_detalhes'), 
]


