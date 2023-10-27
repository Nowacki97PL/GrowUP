from django.contrib import admin

from gym.models import Trainer, TrainerServices, TrainerAppointment


admin.site.register(Trainer)
admin.site.register(TrainerServices)
admin.site.register(TrainerAppointment)

