from django import forms
from django.core import validators
def namestart(value):
    if value[0].upper()!='G':
        raise forms.ValidationError("Invalid")
class ValidationForm(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(3),namestart])