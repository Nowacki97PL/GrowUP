from django.contrib import admin

from gym.models import Dietician, DieticianServices, MentalTrainer, MentalTrainerServices, Trainer, TrainerServices, \
    TrainerAppointment, WorkingHour


class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ['time', 'is_available']


admin.site.register(Trainer)
admin.site.register(Dietician)
admin.site.register(MentalTrainer)
admin.site.register(MentalTrainerServices)
admin.site.register(TrainerServices)
admin.site.register(DieticianServices)
admin.site.register(TrainerAppointment)
admin.site.register(WorkingHour, WorkingHourAdmin)
