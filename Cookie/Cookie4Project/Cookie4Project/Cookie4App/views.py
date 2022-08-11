from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request,'Cookie4App/home.html')
def collegeView(request):
    name=request.GET['name']
    response=render(request,'Cookie4App/college.html',{'name':name})
    response.set_cookie('name',name)
    return response
def markView(request):
    name=request.COOKIES['name']
    response=render(request,'Cookie4App/mark.html',{'name':name})
    college=request.GET['college']
    response.set_cookie('college',college)
    return response
def emailView(request):
    name=request.COOKIES['name']
    response=render(request,'Cookie4App/email.html',{'name':name})
    mark=request.GET['mark']
    response.set_cookie('mark',mark)
    return response
def finalView(request):
    name=request.COOKIES['name']
    college=request.COOKIES['college']
    mark=request.COOKIES['mark']
    email=request.GET['email']
    return render(request,'Cookie4App/final.html',{'name':name,'college':college,'mark':mark,'email':email})