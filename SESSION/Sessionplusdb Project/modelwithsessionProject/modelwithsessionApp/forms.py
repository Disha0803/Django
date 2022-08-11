from dataclasses import fields
from django import forms
from modelwithsessionApp.models import StudentForm
class StuForm(forms.ModelForm):
    class Meta:
        model=StudentForm
        fields='__all__'
class DetailsForm(forms.Form):
    Name=forms.CharField()