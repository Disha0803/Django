from django.shortcuts import render
from StudentFormApp.forms import Studentform
# Create your views here.
def Studentview(request):
    form=Studentform()
    check=False
    x=0
    y=0
    z=0
    tot=0
    avg=0
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            x=form.cleaned_data['Marks_Maths']
            y=form.cleaned_data['Marks_Science']
            z=form.cleaned_data['Marks_Computer']
            tot=x+y+z
            avg="{:.2f}".format(tot/3)
            check=True
    return render(request,'StudentFormApp/index.html',{'form':form,'x':x ,'y':y ,'z':z ,'tot':tot,'avg':avg,'check':check})