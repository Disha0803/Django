from django.shortcuts import render
from FilterApp.models import Filter
# Create your views here.
def display(request):
    # f=Filter()
    data=Filter.objects.all
    return render(request,'FilterApp/index.html',{'data':data})
