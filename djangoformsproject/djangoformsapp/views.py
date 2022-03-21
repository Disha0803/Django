from django.shortcuts import render
from djangoformsapp.forms import StudentForm
# Create your views here.
def display(request):
    obj=StudentForm()
    my_dict={'form':obj}
    return render(request,'djangoformsapp/form.html',context=my_dict)