from django.contrib import admin
from insert.models import ExhibitorList,Event
# Register your models here.
class Inline(admin.TabularInline):
    model = ExhibitorList
    extra = 3

class EventAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['event_text']}),('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    list_display = ('event_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

    inlines = [Inline]

admin.site.register(Event, EventAdmin)
admin.site.register(ExhibitorList)