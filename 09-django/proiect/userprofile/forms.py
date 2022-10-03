from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}),
        }

