from django.contrib import admin
from ModelApp2.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','saddr','smarks']
admin.site.register(Student,StudentAdmin)