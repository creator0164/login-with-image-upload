from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from .models import Account


class AccountForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'style': 'font-size : 17px;'}), label='')
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'style': 'font-size : 17px;'}), label='')
    password = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Password', 'type': 'password', 'style': 'font-size : 17px;'}), label='')

    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'password',
        ]
