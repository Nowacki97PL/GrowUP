from django.contrib import admin

from gym.models import Dietician, DieticianServices, MentalTrainer, MentalTrainerServices, Trainer, TrainerServices, \
    TrainerAppointment

admin.site.register(Trainer)
admin.site.register(Dietician)
admin.site.register(MentalTrainer)
admin.site.register(MentalTrainerServices)
admin.site.register(TrainerServices)
admin.site.register(DieticianServices)
admin.site.register(TrainerAppointment)

