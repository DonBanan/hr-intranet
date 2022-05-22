from django import forms

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class EditUserSESForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_ses']
