from django.contrib import admin
from Genesis.models import RegistrationForm
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['Name','Email','Mobile','Redgno','Event']
admin.site.register(RegistrationForm,RegistrationAdmin)