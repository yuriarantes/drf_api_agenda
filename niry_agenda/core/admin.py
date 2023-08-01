from django.contrib import admin
from django.utils.formats import time_format, get_format

from .models import Scheduling, Schedule, Store
#from .actions import make_cancelled

class StoreAdmin(admin.ModelAdmin):
    list_display=['id','social_name','cnpj','active']
    search_fields=['social_name','cnpj']

class ScheduleAdmin(admin.ModelAdmin):
    list_display=['id','store','day','first_start_at','first_end_at','last_start_at','last_end_at']
    search_fields=['store','day']
    list_filter=['store']

class SchedulingAdmin(admin.ModelAdmin):
    list_display = ['id','scheduling_date', 'name', 'email', 'phone','active']
    list_filter = ['scheduling_date']
    search_fields = ['scheduling_date','name']
    list_editable = ['name']
    
    def scheduling_cancel(modeladmin, request, queryset):
        queryset.update(active=False)

    def scheduling_activate(modeladmin, request, queryset):
        queryset.update(active=True)

    scheduling_cancel.short_description = "Cancelar agendamento"
    scheduling_activate.short_description = "Ativar agendamento"

    actions = [scheduling_cancel,scheduling_activate]

admin.site.register(Scheduling, SchedulingAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Schedule, ScheduleAdmin)
