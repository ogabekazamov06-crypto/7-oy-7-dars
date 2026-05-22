from django.contrib.auth.models import User
from django import forms
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegisterForm(UserCreationForm):
    age = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'style': 'padding: 10px;'
            }),
            'email': forms.EmailInput(attrs={
                'style': 'padding: 10px;'
            }),
            'password1': forms.PasswordInput(attrs={
                'style': 'padding: 10px;',
                'placeholder': 'Parol kiriting'
            }),
            'password2': forms.PasswordInput(attrs={
                'style': 'padding: 10px;',
                'placeholder': 'Parolni tasdiqlang'
            }),
        }