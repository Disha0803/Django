from urllib import response
from django.shortcuts import render
from Cookie2App.forms import CookieForm
# Create your views here.
def namedisplay(request):
    form=CookieForm()
    d=''
    if d in request.COOKIES:
        data=request.COOKIES['data']
    else:
        form=CookieForm()
        if request.method=='POST':
            d=request.POST.get('Name')
        data=d
    response=render(request,'Cookie2App/index.html',{'form':form,'data':data})
    response.set_cookie('data',data)
    return response
def display(request):
    form=CookieForm()
    result=request.COOKIES['data']
    response=render(request,'Cookie2App/index2.html',{'form':form,'result':result})
    return response 
def display2(request):
    form=CookieForm()
    result=request.COOKIES['data']
    response=render(request,'Cookie2App/index3.html',{'form':form,'result':result})
    return response 