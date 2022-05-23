from django import forms
class Studentform(forms.Form):
    name=forms.CharField()
    opass=forms.CharField()
    cpass=forms.CharField()

    def clean(self):
        x=super().clean()
        p=x['opass']
        cp=x['cpass']
        if p!=cp:
            raise forms.ValidationError("Passwords not matching!")
