from django.shortcuts import render
from Genesis.forms import Regd
def genreg(request):
    form=Regd()
    if request.method == "POST":
        form=Regd(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Genesis/register.html',{'form':form})