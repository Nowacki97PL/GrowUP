from django.contrib import admin

from gym.models import Dietician, MentalTrainer, MentalTrainerServices, Trainer, TrainerServices

admin.site.register(Trainer)
admin.site.register(Dietician)
admin.site.register(MentalTrainer)
admin.site.register(MentalTrainerServices)
admin.site.register(TrainerServices)
admin.site.register(DieticianServices)

