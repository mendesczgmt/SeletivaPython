from django.shortcuts import render, redirect, get_object_or_404

from usuarios.forms import LoginForms, CadastroForms, AlteraForms
from django.db import models
from usuarios.models import Pessoa
from django.contrib import messages


def index(request):
    return render(request, 'usuarios/index.html')


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        if request.method == 'POST':
            form = LoginForms(request.POST)
            if form.is_valid():
                email = form.cleaned_data['emailLogin']
                senha = form.cleaned_data['senhaLogin']

                try:
                    pessoa = Pessoa.objects.get(email=email, senha=senha)
                    messages.success(request, ' usuário logado com sucesso!')
                    return redirect('listar')
                except:
                    messages.error(
                        request, 'Erro ao efetuar login. Email ou senha incorretos.')
                    return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            email = form['emailCadastro'].value()
            nome = form['nomeCadastro'].value()
            senha = form['senhaCadastro'].value()
            idDiscord = form['idDiscordCadastro'].value()

            if Pessoa.objects.filter(email=email).exists():
                messages.error(request, 'Email já existente')
                return redirect('cadastro')

            if Pessoa.objects.filter(idDiscord=idDiscord).exists():
                messages.error(request, 'id Discord já existente')
                return redirect('cadastro')

            else:
                nova_pessoa = Pessoa(nome=nome, senha=senha,
                                     email=email, idDiscord=idDiscord)
                nova_pessoa.save()
                messages.success(request, ' usuário cadastrado com sucesso!')
                return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})


def listar(request):
    usuarios = Pessoa.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})


def alterar(request, id):
    usuario = Pessoa.objects.get(id=id)
    form = AlteraForms(instance=usuario)

    if request.method == 'POST':
        form = AlteraForms(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'usuário editado com sucesso')
            return redirect('index')

    return render(request, 'usuarios/alterar.html', {'form': form, 'id': id})

def excluir(request, id):
    usuario = get_object_or_404(Pessoa, id=id)
    usuario.delete()
    return redirect('listar')
