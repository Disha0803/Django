from django.shortcuts import render
from modelwithsessionApp.models import StudentForm
from modelwithsessionApp.forms import *
# Create your views here.
def StudentView(request):
    form=StuForm()
    if request.method=='POST':
        form=StuForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'modelwithsessionApp/home.html',{'form':form})
def FormView(request):
    list=StudentForm.objects.all()
    return render(request,'modelwithsessionApp/form.html',{'list':list})
def DetailsView(request):
    form=DetailsForm()
    return render(request,'modelwithsessionApp/details.html',{'form':form})
def InfoView(request):
    name=request.GET['Name']
    return render(request,'modelwithsessionApp/info.html',{'name':name})
