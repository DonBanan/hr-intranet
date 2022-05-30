from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput, label=_('Email'))
    password = forms.CharField(widget=forms.PasswordInput)

    fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
    GENDERS = ((True, "Male"), (False, "Female"))
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    gender = forms.ChoiceField(choices=GENDERS, label="Sex (M or F)")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender']


class EditUserSESForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_ses']
