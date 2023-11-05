from django.db import models
from django.db.models import ImageField
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from accounts.models import UserProfile, MyUser
from gym.choices import type_job


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Trainer(BaseModel):
    avatar = ImageField(upload_to="avatars/", null=True, blank=True)
    avatar_thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(125, 200)],
        format="JPEG",
        options={"quality": 100},
    )
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.trainer.first_name} {self.trainer.last_name} - {self.job}"


class TrainerServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(BaseModel):
    date = models.DateField()
    hour = models.TimeField()


class TrainerAppointment(Appointment):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    services = models.ForeignKey(TrainerServices, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.services}"
