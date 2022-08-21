from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from MiniApp.forms import SignupForm
from django.http import HttpResponseRedirect
# Create your views here.
def eduView(request):
    return render(request,'MiniApp/base.html')

def homeView(request):
    return render(request,'MiniApp/home.html')

def aboutusView(request):
    return render(request,'MiniApp/aboutus.html')

def contactusView(request):
    return render(request,'MiniApp/contactus.html')
@login_required
def coursesView(request):
    return render(request,'MiniApp/courses.html')
def logoutView(request):
    return render(request,'MiniApp/logout.html')  

def SignupView(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'MiniApp/signup.html',{'form':form})
@login_required
def dashboardView(request):
    return render(request,'MiniApp/dashboard.html')  

