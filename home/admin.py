from multiprocessing import Event
from django.contrib import admin
from home.models import Contact, Profile, Register ,Event

# Register your models here.
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Event)
admin.site.register(Profile)