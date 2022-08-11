from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeView(request):
    return render(request, 'UserAuthenticationApp/home.html')

def aboutusView(request):
    return render(request, 'UserAuthenticationApp/aboutus.html')

def contactusView(request):
    return render(request, 'UserAuthenticationApp/contactus.html')

@login_required
def studentportalView(request):
    return render(request, 'UserAuthenticationApp/studentportal.html')