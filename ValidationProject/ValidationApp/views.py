from django.shortcuts import render
from ValidationApp.forms import Studentform
# Create your views here.
def Studentview(request):
    form=Studentform()
    check=False
    x=""
    y=""
    z=""
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            x=form.cleaned_data['name']
            y=form.cleaned_data['opass']
            z=form.cleaned_data['cpass']
            check=True
    return render(request,'ValidationApp/index.html',{'form':form,'x':x ,'y':y ,'z':z ,'check':check})