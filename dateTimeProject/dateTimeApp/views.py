from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def displayData(request):
    data=datetime.datetime.now()
    s='<h1>Now the Date and Time is '+str(data)+'</h1>'
    return HttpResponse(s)