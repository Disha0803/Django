from django.shortcuts import render
from GenesisApp.forms import RegistrationForm
from GenesisApp.models import Registration
# Create your views here.

def index(request):
    return render(request,'GenesisApp/homepage.html')

def display(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'GenesisApp/register.html',{'form':form})

def list(request):
    result=Registration.objects.all()
    return render(request,'GenesisApp/list.html',{'result':result})
