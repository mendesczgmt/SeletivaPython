from django import forms
from .models import Pessoa


class LoginForms(forms.Form):
    emailLogin = forms.EmailField(
        label=('Email:'),
        required = True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu email",
                'id': "validationCustomUsername"
            }
        ) 
    )
    senhaLogin = forms.CharField(
        label=('Senha:'),
        required = True,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite sua senha",
                'id': "inputPassword4"
            }
        )
    )

class CadastroForms(forms.Form):
    emailCadastro = forms.EmailField(
        label=('Email:'),
        required = True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu email",
                'id': "validationCustomUsername"
            }
        ) 
    )

    nomeCadastro = forms.CharField(
        label=('Nome:'),
        required = True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu nome",
                'id': "validationCustomUsername"
            }
        ) 
    )

    senhaCadastro = forms.CharField(
        label=('Senha:'),
        required = True,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite sua senha",
                'id': "inputPassword4"
            }
        )
    )

    idDiscordCadastro = forms.CharField(
        label=('ID discord:'),
        required = True,
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu id",
                'id': "validationCustomUsername"
            }
        ) 
    )

class AlteraForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'senha', 'idDiscord']

