from django.contrib.auth.models import User
from django import forms

"""
The line password = forms.CharField(widget=forms.PasswordInput) in your Django form does the following:
Ensures Privacy: Uses a PasswordInput widget to mask the password input, so the password is not visible when typed.
Overrides Default Behavior: Changes the default text input of the CharField to a password input specifically for the password field,
aligning with security practices."""

class Reg(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
