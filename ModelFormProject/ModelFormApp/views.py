from django.shortcuts import render
from ModelFormApp.forms import StudentForm
# Create your views here.
def StudentView(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'ModelFormApp/index.html',{'form':form})
        