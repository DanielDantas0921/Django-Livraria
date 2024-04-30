from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe
from .models import Book

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label= "", widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'E-mail'
        }
           
        
    ), help_text=mark_safe(
        '''
        <span class="form-text text-muted">
            <small> Obrigatório. Digite o seu email. exemplo: exemplo@exemplo.com.</small>
        </span>
        '''
    ))

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
         attrs={
            'class': 'form-control', 'placeholder': 'First Name'
         }
            
        
    ))

    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
         attrs={
             'class': 'form-control', 'placeholder': 'Last Name'
         }
    ))
    
    username = forms.CharField(label = "Usuário: ", max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Digite o usuário'
        }
    ), help_text=mark_safe( ''' <span class="form-text text-muted">
            <small> Obrigatório. 150 caracteres ou menos. Tem que ter Letras, dígitos e alguns characteres.</small>
        </span>'''))
    
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'placeholder': 'DIgite sua senha'
        }
    ), help_text=mark_safe(
        '''
        <ul class="form-text text-muted small">
            <li>Senha deve ser única</li>
            <li>Senha deve conter pelo menos 8 caracteres</li>
            <li>Senha não deve ser totalmente númerica</li>
        </ul>
        '''
    ))
    
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Confirme sua senha'
        }
    ), help_text=mark_safe(
        '''
        <span class="form-text text-muted">
            <small>Digite a mesma senha do campo anterior
        </span>
        '''
    ))
    
    error_messages = {
        'password_mismatch': "As senhas não coincidem"
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].error_messages['password_mismatch'] = self.error_messages['password_mismatch']
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
class AddBookForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Digite o titulo do livro", 'class': 'form-control'
        }
    ), label="")
    
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
            "placeholder": "Digite a descrição do livro", 'class': 'form-control'
        }
    ), label="")
    
    
    year = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(
        attrs={
            "placeholder": "Digite o ano do livro", 'class': 'form-control'
        }
    ), label="")
    
    genre = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Digite o gênero do livro", 'class': 'form-control'
        }
    ), label="")
    
    value = forms.FloatField(required=True, widget=forms.widgets.NumberInput(
        attrs={
            "placeholder": "Digite o valor do livro", 'class': 'form-control'
        }
    ), label="")
    
    class Meta:
        model = Book
        # fields = ('title', 'description', 'year', 'genre', 'value')
        fields = "__all__"
    