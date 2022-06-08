from django import forms
class cookieform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()