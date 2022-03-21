from django.contrib import admin
from InfoApp.models import Informations,Informations2,Informations3
# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    list_display=['info','details']
admin.site.register(Informations,InformationAdmin)
class Information2Admin(admin.ModelAdmin):
    list_display=['info2','details2']
admin.site.register(Informations2,Information2Admin)
class Information3Admin(admin.ModelAdmin):
    list_display=['info3','details3']
admin.site.register(Informations3,Information3Admin)