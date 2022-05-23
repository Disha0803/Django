from dataclasses import fields
from pyexpat import model
from django import forms
from GenesisApp.models import Registration
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'