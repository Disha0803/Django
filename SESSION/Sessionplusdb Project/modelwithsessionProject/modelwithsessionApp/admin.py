from django.contrib import admin
from modelwithsessionApp.models import StudentForm
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['Name','Redg_No','Age','Email','Phn_No']
admin.site.register(StudentForm,StudentAdmin)