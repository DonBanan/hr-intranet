from django import forms

from .models import Niko


class NikoModelForm(forms.ModelForm):
    class Meta:
        model = Niko
        fields = ['mood']
