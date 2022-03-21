from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def displayData(request):
    return HttpResponse('<h3>This is from Third Project')