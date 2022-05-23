from dataclasses import field
from django import forms
from Genesis.models import RegistrationForm
class Regd(forms.ModelForm):
    class Meta:
        model=RegistrationForm
        fields='__all__'