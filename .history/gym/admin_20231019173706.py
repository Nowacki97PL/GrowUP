from django.contrib import admin

from gym.models import Dietician, DieticianServices, MentalTrainer, MentalTrainerServices, Trainer

admin.site.register(Trainer)
admin.site.register(Dietician)
admin.site.register(MentalTrainer)


