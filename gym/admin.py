from django.contrib import admin

from gym.models import Trainer, TrainerServices, TrainerAppointment, WorkingHour


class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ['time', 'is_available']


admin.site.register(Trainer)
admin.site.register(TrainerServices)
admin.site.register(TrainerAppointment)
admin.site.register(WorkingHour, WorkingHourAdmin)
