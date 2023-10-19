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