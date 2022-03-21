from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def displaydata(request):
    resp='<h3>Hello Django... This is my first project</h3>'
    return HttpResponse(resp)