from django.contrib import admin
from PracticeApp.models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=['cid','cname','ccost']
admin.site.register(Course,CourseAdmin)