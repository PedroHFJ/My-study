from .models import TabelaDAS, Despesas, Receita
from datetime import date

def calcular_das(usuario):
    perfil = usuario.perfilmei
    categoria = perfil.categoria_MEI
    ano_atual = 2026

    das = TabelaDAS.objects.filter(
        categoria= categoria,
        ano_vigente=ano_atual
    ).first()

    return das


def gerar_dre(usuario, mes, ano):
    receitas= Receita.objects.filter(usuario=usuario, data__month=mes, data__year=ano )
    despesas=Despesas.objects.filter(usuario=usuario, data__month=mes, data__year=ano)

    receita_bruta=sum(r.valor * r.quantidade_vendida for r in receitas)
    custos_variados=sum(d.valor for d in despesas if d.tipo == 'variavel')
    despesas_fixas=sum(d.valor for d in despesas if d.tipo == 'fixa')

    das = calcular_das(usuario)
    valor_das=  das.valor_mensal if das else 0

    lucro_liquido=receita_bruta - custos_variados - despesas_fixas - valor_das


    return {
        'receita_bruta' : receita_bruta,
        'custos_variados' : custos_variados,
        'despesas_fixas' : despesas_fixas,
        'valor_das' : valor_das,
        'lucro_liquido' : lucro_liquido,
    }


def historico_dre(usuario, meses=6):
    hoje = date.today()
    resultados = []
    mes = hoje.month
    ano = hoje.year


    for i in range(meses):
        dados = gerar_dre(usuario, mes, ano)
        label = f"{mes:02d}/{ano}"
        resultados.append({'mes' : label, **dados})

        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1 

    resultados.reverse()
    return resultados

