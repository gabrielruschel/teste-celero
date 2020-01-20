from django.contrib import admin
from .models import Athlete,Event
# Register your models here.
admin.site.register(Athlete)

class EventAdmin(admin.ModelAdmin):
    raw_id_fields = ('athlete',)

admin.site.register(Event,EventAdmin)
