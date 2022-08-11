from multiprocessing.sharedctypes import Value
from os import name
from urllib import response
from django.shortcuts import render

from CartApp.forms import itemsForm
# Create your views here.
def homeView(request):
    return render(request,'CartApp/home.html')
def apparelsView(request):
    return render(request,'CartApp/apparels.html')
def itemsView(request):
    form=itemsForm()
    r=request.GET.get('name')
    return render(request,'CartApp/items.html',{'form':form,'response':r})
def cartView(request):
    form=itemsForm()
    size=''
    quantity=''
    if request.method=='POST':
        form=itemsForm(request.POST)
        if form.is_valid():
            size=form.cleaned_data['Size']
            quantity=form.cleaned_data['Quantity']
    
    return render(request,'CartApp/cart.html',{'size':size,'quantity':quantity})
