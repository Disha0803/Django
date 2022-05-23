from django.contrib import admin
from ModelFormApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile']
admin.site.register(Student,StudentAdmin)