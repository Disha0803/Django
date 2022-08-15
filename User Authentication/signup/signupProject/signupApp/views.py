from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from signupApp.forms import Signupform
from django.http import HttpResponseRedirect
# Create your views here.
def homeView(request):
    return render(request, 'signupApp/home.html')

@login_required
def aboutusView(request):
    return render(request, 'signupApp/aboutus.html')

@login_required
def contactusView(request):
    return render(request, 'signupApp/contactus.html')

# @login_required
# def studentportalView(request):
#     return render(request, 'signupApp/studentportal.html')

@login_required
def profileView(request):
    return render(request, 'signupApp/profile.html')

def logoutView(request):
    return render(request, 'signupApp/logout.html')

def signupView(request):
    form=Signupform()
    if request.method== 'POST':
        form=Signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'signupApp/signup.html',{'form':form})