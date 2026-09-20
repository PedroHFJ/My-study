from django.urls import path
from . import views

urlpatterns = [
    path('despesas/', views.listar_despesas, name='listar_despesas'),
    path('despesas/nova', views.criar_despesas, name='criar_despesas'),
    path('despesas/<int:pk>/editar', views.editar_despesa, name='editar_despesa'),
    path('despesas/<int:pk>/excluir', views.excluir_despesa, name='excluir_despesa'),

    path('receita/', views.listar_receita, name='listar_receita'),
    path('receita/criar_receitas', views.criar_receitas, name='criar_receitas')

]