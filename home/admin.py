from multiprocessing import Event
from django.contrib import admin
from home.models import Contact, Eventlogin, Profile, Register ,Event
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Event)
admin.site.register(Profile)
@admin.register(Eventlogin)
class usrdet(ImportExportModelAdmin):
    pass
