from django.contrib import admin

from gym.models import Trainer, TrainerServices, TrainerAppointment, MentalTrainer, MentalTrainerServices, \
    MentalTrainerAppointment, Dietitian, DietitianServices, DietitianAppointment

admin.site.register(Trainer)
admin.site.register(TrainerServices)
admin.site.register(TrainerAppointment)
admin.site.register(MentalTrainer)
admin.site.register(MentalTrainerServices)
admin.site.register(MentalTrainerAppointment)
admin.site.register(Dietitian)
admin.site.register(DietitianServices)
admin.site.register(DietitianAppointment)
