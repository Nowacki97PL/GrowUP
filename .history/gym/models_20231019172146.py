from django.db import models

from accounts.models import UserProfile
from gym.choices import type_job

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Trainer(BaseModel):
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)

    def __str__(self):
        return f"{self.trainer.first_name} {self.trainer.last_name} - {self.job}"
        
class Dietician(BaseModel):
    dietician = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)

    def __str__(self):
        return f"{self.dietician.first_name} {self.dietician.last_name} - {self.job}"


class MentalTrainer(BaseModel):
    mental_trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)

    def __str__(self):
        return f"{self.mental_trainer.first_name} {self.mental_trainer.last_name} - {self.job}"
    

class Services(BaseModel):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

class TrainerServices(Services):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    

class DieticianServices(Services):
    trainer = models.ForeignKey(Dietician, on_delete=models.CASCADE)