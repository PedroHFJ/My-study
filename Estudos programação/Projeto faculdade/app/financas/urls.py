from django.urls import path
from . import views


urlpatterns = [

#DESPESA

    path('despesas/', views.listar_despesas, name='listar_despesas'),
    path('despesas/nova', views.criar_despesas, name='criar_despesas'),
    path('despesas/<int:pk>/editar', views.editar_despesa, name='editar_despesa'),
    path('despesas/<int:pk>/excluir', views.excluir_despesa, name='excluir_despesa'),

#RECEITA 

    path('receita/', views.listar_receita, name='listar_receita'),
    path('receita/criar_receitas', views.criar_receitas, name='criar_receitas'),
    path('receita/<int:pk>/editar_receita', views.editar_receita, name='editar_receita'),
    path('receita/<int:pk>/excluir_receita', views.excluir_receita, name='excluir_receita'),

#IMPOSTO

    path('imposto/', views.imposto_atual, name='imposto_atual'),


#DRE

    path('dre/', views.dre_mensal, name='dre_mensal'),


#CADASTRO

   
    path('cadastro/', views.cadastro, name='cadastro'),


#GRAFICO 
    path('grafico/', views.grafico_mensal, name='grafico_mensal'),

    
]


