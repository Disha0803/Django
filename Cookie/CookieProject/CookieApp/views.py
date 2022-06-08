from itertools import count
from unittest import result
from django.shortcuts import render
from CookieApp.forms import cookieform
# Create your views here.

def pagecount(request):
    if 'count' in request.COOKIES:
        result=int(request.COOKIES['count'])+1
    else:
        result=1
    response=render(request,'CookieApp/pagecount.html',{'result':result})
    response.set_cookie('count',result)
    return response
def display(request):
    form=cookieform()
    result=request.COOKIES['count']
    response=render(request,'CookieApp/index.html',{'form':form,'result':result})
    return response 