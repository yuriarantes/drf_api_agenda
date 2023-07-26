from django.contrib import admin

from .models import Scheduling
#from .actions import make_cancelled

def scheduling_cancel(modeladmin, request, queryset):
    queryset.update(active=False)

def scheduling_activate(modeladmin, request, queryset):
    queryset.update(active=True)

scheduling_cancel.short_description = "Cancelar agendamento"
scheduling_activate.short_description = "Ativar agendamento"

class SchedulingAdmin(admin.ModelAdmin):
    list_display = ['id','scheduling_date', 'name', 'email', 'phone','active']
    list_filter = ['name','email','phone']
    search_fields = ['scheduling_date','name']
    list_editable = ['name']
    actions = [scheduling_cancel,scheduling_activate]

admin.site.register(Scheduling, SchedulingAdmin)
