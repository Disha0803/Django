from urllib import response
from django.shortcuts import render
from LoginSignupApp.forms import signup
from LoginSignupApp.forms import login
# Create your views here.
def signupview(request):
    form1=signup()
    d=''
    f=''
    if d in request.COOKIES:
        if f in request.COOKIES:
            em=request.COOKIES['em']
            p=request.COOKIES['p']
    else:
        form1=signup()
        if request.method=="POST":
            d=request.POST.get('Email')
            f=request.POST.get('Password')
        em=d
        p=f
        response=render(request,'LoginSignupApp/signup.html',{'form1':form1})
        response.set_cookie('em',em)
        response.set_cookie('p',p)
        
    return response
def homeview(request):
    return render(request,'LoginSignupApp/homepage.html')
def loginview(request):
    form2=login()
    result=0
    ec=''
    pc=''
    # response=render(request,'LoginSignupApp/login.html',{'form2':form2})
    if request.method=="POST":
        form2=login(request.POST)
        emailchk=form2.cleaned_data('Email')
        passwordchk=form2.cleaned_data('Password')
        ec=request.COOKIES['em']
        pc=request.COOKIES['p']
        if emailchk==ec and passwordchk==pc:
            result=1
            # response=render(request,'LoginSignupApp/result.html')
        else:
            result=0
            # response=render(request,'LoginSignupApp/homepage.html',{'form2':form2})
        
    return render(request,'LoginSignupApp/login.html',{'form2':form2,'result':result})