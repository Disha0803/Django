import imp
from django.contrib import admin
from ModelApp3.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','eaddr','esal']
admin.site.register(Employee,EmployeeAdmin)