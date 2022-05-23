from django.contrib import admin
from GenesisApp.models import Registration
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['Name','Email','Mobile','Redgno','Event']
admin.site.register(Registration,RegistrationAdmin)