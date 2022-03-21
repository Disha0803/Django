from django.shortcuts import render
from PracticeApp.models import Course
# Create your views here.
def display(request):
    course_list=Course.objects.all()
    my_dict={'course_list':course_list}
    return render(request,'PracticeApp/index.html',context=my_dict)