from django.contrib import admin

from gym.models import Dietician, MentalTrainer, Trainer

admin.site.register(Trainer)
admin.site.register(Dietician)
admin.site.register(MentalTrainer)
admin.site.register(MentalTrainerServices)
admin.site.register(Trainer)
admin.site.register(MentalTrainer)

