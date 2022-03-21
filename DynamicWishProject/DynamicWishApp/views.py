from django.shortcuts import render
import datetime
# Create your views here.
def displayWish(request):
    data=datetime.datetime.now().hour
    s='Hello '
    if data<12:
        s=s+'Good Morning'
    elif data<17:
        s=s+'Good Afternoon'
    elif data<21:
        s=s+'Good Evening'
    else:
        s=s+'Good Night'
    s=s+''
    dict={'wish':s,'date':data}
    return render(request, 'DynamicWishApp/wish.html',context=dict)