from django import forms
class NameForm(forms.Form):
    Name=forms.CharField()
class CollegeForm(forms.Form):
    College=forms.CharField()
class MarksForm(forms.Form):
    Marks=forms.IntegerField()
class EmailForm(forms.Form):
    Email=forms.CharField()