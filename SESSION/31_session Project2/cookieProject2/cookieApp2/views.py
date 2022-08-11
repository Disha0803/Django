from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request,'cookieApp2/home.html')


def collegeView(request):
    name=request.GET['name']
    request.session['name']=name
    return render(request,'cookieApp2/college.html',{'name':name})
    
def emailView(request):
    college=request.GET['college']
    request.session['college']=college
    name=request.session['name']
    return render(request,'cookieApp2/email.html',{'name':name})

def finalView(request):
    email=request.GET['email']
    request.session['email']=email
    name=request.session['name']
    college=request.session['college']
    return render(request,'cookieApp2/final.html',{'name':name,'college':college,'email':email})
    


    
