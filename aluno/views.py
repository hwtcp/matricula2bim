from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .form import AlunoForm

def listar_alunos(request):
    alunos= Aluno.objects.all()
    return render(request, "index.html", {'alunos': alunos})

def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            print("Aluno salvo:", aluno)
            return redirect('listar_alunos')
        else:
            print("Erros do formulário:", form.errors)
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})

def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'cadastrar_aluno.html', {'form': form})

def aluno_excluir(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('listar_alunos')

def aluno_desativar(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.status = not aluno.status 
    aluno.save()
    return redirect("listar_alunos")

def aluno_detalhes(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno_detalhes.html', {'aluno': aluno})

