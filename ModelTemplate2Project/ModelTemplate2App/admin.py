from django.contrib import admin
from ModelTemplate2App.models import Classical_Dance_Forms,Modern_Dance
# from ModelTemplate2App.models import Modern_Dance
# Register your models here.
class ClassicalAdmin(admin.ModelAdmin):
    list_display=['dname','dorigin','dcost']
admin.site.register(Classical_Dance_Forms,ClassicalAdmin)
class ModernAdmin(admin.ModelAdmin):
    list_display=['mname','morigin','mcost']
admin.site.register(Modern_Dance,ModernAdmin)