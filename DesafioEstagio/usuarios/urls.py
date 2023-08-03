from django.urls import path
from usuarios.views import index, cadastro, login, listar, excluir, alterar

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('listar', listar, name='listar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
    path('alterar/<int:id>/', alterar, name='alterar')
]
