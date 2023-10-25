from django.db import models

from accounts.models import MyUser
from choices import type_job

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Trainer(BaseModel):
    trainer = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)

    def __str__(self):
            return f"{self.trainer.first_name} {self.trainer.last_name} - {self.job}"
        
class Dietician(BaseModel):
    dietician = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)

    def __str__(self):
        if self.dietician:
            return f"{self.dietician.first_name} {self.dietician.last_name} - {self.job}"


class MentalTrainer(BaseModel):
    mental_trainer = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)

    def __str__(self):
        if self.mental_trainer:
            return f"{self.mental_trainer.first_name} {self.mental_trainer.last_name} - {self.job}"