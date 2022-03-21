from django import forms
Courses=[
    ('Btech','Btech'),
    ('BCA','BCA'),
    ('Mtech','Mtech'),
    ('MCA','MCA')
]
Gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]
class StudentForm(forms.Form):
    Name=forms.CharField()
    Registration_Number=forms.IntegerField()
    Course=forms.CharField(widget=forms.Select(choices=Courses))
    Gender=forms.CharField(widget=forms.RadioSelect(choices=Gender))
    Age=forms.IntegerField()
    Address=forms.CharField()
    Email=forms.CharField()
    Phone_Number=forms.IntegerField()
 
