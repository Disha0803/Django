
from django.shortcuts import render
from session3app.forms import *
# Create your views here.
def homeView(request):
    form=NameForm()
    return render(request,'session3app/home.html',{'form':form})
def collegeView(request):
    form=CollegeForm()
    name=''
    if request.method=="POST":
        form=CollegeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            request.session['name']=name
    return render(request,'session3app/college.html',{'form':form,'name':name})
def marksView(request):
    form=MarksForm()
    Name=request.session['Name']
    if request.method=="POST":
        form=MarksForm(request.POST)
        if form.is_valid():
            College=form.cleaned_data['College']
            request.session['College']=College
    return render(request,'session3app/marks.html',{'form':form,'College':College,'name':Name})