from django import forms
class Studentform(forms.Form):
    Full_Name=forms.CharField()
    Redg_Numb=forms.IntegerField()
    Marks_Maths=forms.FloatField()
    Marks_Science=forms.FloatField()
    Marks_Computer=forms.FloatField()
    
    def clean_Full_Name(self):
        name=self.cleaned_data['Full_Name']
        if len(name)<3:
            print("Invalid")
            raise forms.ValidationError("Invalid Name")
        return name

    def clean_Marks_Maths(self):
        marks=self.cleaned_data['Marks_Maths']
        if marks>100:
            print("Invalid")
            raise forms.ValidationError("Invalid marks")
        return marks

    def clean_Marks_Science(self):
        marks=self.cleaned_data['Marks_Science']
        if marks>100:
            print("Invalid")
            raise forms.ValidationError("Invalid marks")
        return marks

    def clean_Marks_Computer(self):
        marks=self.cleaned_data['Marks_Computer']
        if marks>100:
            print("Invalid")
            raise forms.ValidationError("Invalid marks")
        return marks