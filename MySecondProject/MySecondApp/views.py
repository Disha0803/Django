from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def displayData(request):
    resp="<h3>Hello... This is my Second Project</h3>"
    return HttpResponse(resp)