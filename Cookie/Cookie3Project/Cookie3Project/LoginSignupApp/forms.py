from django import forms
class signup(forms.Form):
    Name=forms.CharField()
    Age=forms.IntegerField()
    Address=forms.CharField()
    Email=forms.EmailField()
    Password=forms.CharField()
    ConfirmPassword=forms.PasswordInput()
class login(forms.Form):
    Email=forms.EmailField()
    Password=forms.CharField()