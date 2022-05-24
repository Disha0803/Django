from django.contrib import admin
from FilterApp.models import Filter
# Register your models here.
class FilterAdmin(admin.ModelAdmin):
    list_display=['Name','Age','Email','Course','DOB']
admin.site.register(Filter,FilterAdmin)
