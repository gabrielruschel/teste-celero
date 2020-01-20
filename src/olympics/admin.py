from django.contrib import admin
from .models import Athlete,Event
# Register your models here.

class AthleteAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Athlete, AthleteAdmin)

class EventAdmin(admin.ModelAdmin):
    autocomplete_fields = ['athlete',]

admin.site.register(Event,EventAdmin)
