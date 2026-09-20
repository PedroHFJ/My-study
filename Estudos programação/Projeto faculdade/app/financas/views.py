from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Despesas, Receita
from .forms import DespesaForm, ReceitaForm, CadastroForm, PerfilMEIForm
from .calculos import calcular_das, gerar_dre, historico_dre
from datetime import date
import json




@login_required
def listar_despesas(request):
    despesas = Despesas.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'financas/listar_despesas.html', {'despesas': despesas})

# Create your views here.

#DESPESAS
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

#RECEITA


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
    return render(request, 'financas/form_receita.html', {'form' : form})

@login_required
def editar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk, usuario = request.user)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            return redirect('listar_receita')
    else:
        form = ReceitaForm(instance=receita)
    return render(request, 'financas/form_receita.html', {'form' : form})

@login_required
def excluir_receita(request,pk):
    receita = get_object_or_404(Receita, pk=pk, usuario = request.user)
    if request.method == 'POST':
        receita.delete()
        return redirect('listar_receita')
    return render(request, 'financas/confirmar_exclusao_receita.html', {'receita' : receita})
  

#CALCULO DE IMPOSTO


@login_required
def imposto_atual(request):
    das = calcular_das(request.user)
    return render(request, 'financas/imposto_atual.html', {'das' : das})


#DRE

@login_required
def dre_mensal(request):
    hoje = date.today()
    dados = gerar_dre(request.user, hoje.month, hoje.year)
    return render(request, 'financas/dre_mensal.html', {'dre' : dados})

#CADASTRO

def cadastro(request):
    if request.method == 'POST':
        user_form = CadastroForm(request.POST)
        perfil_form = PerfilMEIForm(request.POST)
        if user_form.is_valid() and perfil_form.is_valid():
            usuario = user_form.save()
            perfil = perfil_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            return redirect('login')
    else:
        user_form = CadastroForm()
        perfil_form = PerfilMEIForm()
        form = CadastroForm()
    return render(request, 'financas/cadastro.html', 
                  {
                      'user_form' : user_form,
                      'perfil_form' : perfil_form,
                  })


#GRAFICO

@login_required
def grafico_mensal(request):
    historico = historico_dre(request.user, 6)

    labels = [h['mes'] for h in historico]
    receitas = [float(h['receita_bruta']) for h in historico]
    despesas = [float(h['custos_variados'] + h['despesas_fixas']) for h in historico]

    context = {
        'labels' : json.dumps(labels),
        'receitas' : json.dumps(receitas),
        'despesas' : json.dumps(despesas),
    }

    return render(request, 'financas/grafico_mensal.html', context)