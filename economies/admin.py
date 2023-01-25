from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class EventResource(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        fields = ('id', 'title', 'description', 'read_code', 'update_code', 'start_time', 'end_time', 'created', 'last_updated',)
        model = Event

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource
    readonly_fields = ('id',)
    search_fields = ('title', 'description', 'read_code', 'update_code',)
    list_display = ('id', 'title', 'description', 'read_code', 'update_code', 'start_time', 'end_time', 'created', 'last_updated',)
    list_filter = ('start_time', 'end_time', 'created', 'last_updated',)

class EconomicModelResource(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        fields = ('id', 'event', 'economic_model', 'economic_model_raw_data', 'notes', 'created', 'last_updated',)
        model = EconomicModel

@admin.register(EconomicModel)
class EconomicModelAdmin(ImportExportModelAdmin):
    resource_class = EconomicModelResource
    readonly_fields = ('id',)
    search_fields = ('event', 'notes',)
    list_display = ('id', 'event', 'economic_model', 'economic_model_raw_data', 'notes', 'created', 'last_updated',)
    list_filter = ('event', 'created', 'last_updated',)