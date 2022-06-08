from django import forms
class CookieForm(forms.Form):
    Name=forms.CharField(max_length=50)
    Email=forms.EmailField()
    Phone=forms.IntegerField()