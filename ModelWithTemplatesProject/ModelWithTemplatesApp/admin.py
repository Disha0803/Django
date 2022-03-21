from django.contrib import admin
from ModelWithTemplatesApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['sname','sage','sclass','sroll']
admin.site.register(Student,StudentAdmin)