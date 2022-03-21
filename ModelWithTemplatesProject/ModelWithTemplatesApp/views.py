from django.shortcuts import render
from ModelWithTemplatesApp.models import Student
# Create your views here.
def display(request):
    student_list=Student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'ModelWithTemplatesApp/student.html',context=my_dict)