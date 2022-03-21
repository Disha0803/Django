from django.shortcuts import render
from InfoApp.models import Informations,Informations2,Informations3
# Create your views here.
def display(request):
    info_list=Informations.objects.all()
    dict={'info_list':info_list}
    return render(request,'InfoApp/info.html',context=dict)
def display2(request):
    info_list2=Informations2.objects.all()
    dict={'infolist':info_list2}
    return render(request,'InfoApp/secondpage.html',context=dict)
def display3(request):
    info_list3=Informations3.objects.all()
    dict={'infolist2':info_list3}
    return render(request,'InfoApp/secondpage.html',context=dict)

