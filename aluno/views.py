from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .form import AlunoForm
from django.core.paginator import Paginator
from django.db.models import Q

def listar_alunos(request):
    busca = request.GET.get('busca', '')
    curso = request.GET.get('curso', '')

    alunos = Aluno.objects.all()

    if busca:
        alunos = alunos.filter(
            Q(nome__icontains=busca) | Q(matricula__icontains=busca)
        )

    if curso:
        alunos = alunos.filter(curso=curso)

    alunos = alunos.order_by('id') 

    paginator = Paginator(alunos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    inicio = (page_obj.number - 1) * paginator.per_page + 1
    fim = inicio + len(page_obj.object_list) - 1
    total = paginator.count

    context = {
        'page_obj': page_obj,
        'busca': busca,
        'curso': curso,
        'inicio': inicio,
        'fim': fim,
        'total': total,
    }

    return render(request, "index.html", context)


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

