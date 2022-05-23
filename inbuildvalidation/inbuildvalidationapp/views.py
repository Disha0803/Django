from django.shortcuts import render
from inbuildvalidationapp.forms import ValidationForm
# Create your views here.
def Valid(request):
    form=ValidationForm()
    check=False
    x=''
    if request.method=='POST':
        form=ValidationForm(request.POST)
        if form.is_valid():
            x=form.cleaned_data['name']
            check=True
    return render(request,'inbuildvalidationapp/index.html',{'form':form,'x':x,'check':check})
