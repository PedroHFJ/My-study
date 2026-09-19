from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Despesas, Receita
from .forms import DespesaForm, ReceitaForm


@login_required
def listar_despesas(request):
    despesas = Despesas.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'financas/listar_despesas.html', {'despesas': despesas})

# Create your views here.
@login_required
def criar_despesas(request):
    if request.method == 'POST':
        form  = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm()
    return render(request, 'financas/form_despesa.html', {'form' : form})


@login_required
def editar_despesa(request, pk):
    despesa = get_object_or_404(Despesas, pk=pk, usuario = request.user)
    form = DespesaForm(request.POST, instance=despesa)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
    if form.is_valid():
        form.save()
        return redirect('listar_despesas')
    else:
        form = DespesaForm(instance=despesa)
    return render(request, 'financas/form_despesa.html', {'form': form})

@login_required
def excluir_despesa(request,pk):
    despesa = get_object_or_404(Despesas, pk=pk, usuario = request.user )
    if request.method == 'POST':
        despesa.delete()
        return render(request, 'financas/confirmar_exclusao.html', {"despesa" : despesa})
    return render(request, 'financas/confirmar_exclusao.html', {'despesa': despesa})


@login_required
def listar_receita(request):
    receita = Receita.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'financas/listar_receita.html', {'receita' : receita})

@login_required
def criar_receitas(request):
    if request.method=='POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.usuario = request.user
            receita.save() 
            return redirect('listar_receita')
        else:
            form = ReceitaForm()
            return render(request, 'financas/listar_receita.html', {'form' : form})


