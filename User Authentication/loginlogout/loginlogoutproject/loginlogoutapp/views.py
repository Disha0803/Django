from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def homeView(request):
    return render(request, 'loginlogoutapp/home.html')

@login_required
def aboutusView(request):
    return render(request, 'loginlogoutapp/aboutus.html')

@login_required
def contactusView(request):
    return render(request, 'loginlogoutapp/contactus.html')

# @login_required
# def studentportalView(request):
#     return render(request, 'loginlogoutapp/studentportal.html')

@login_required
def profileView(request):
    return render(request, 'loginlogoutapp/profile.html')

def logoutView(request):
    return render(request, 'loginlogoutapp/logout.html')