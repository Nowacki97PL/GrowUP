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

    class Meta:
        verbose_name = "Trener personalny"
        verbose_name_plural = "Trenerzy personalni"


class MentalTrainer(Trainer):
    class Meta:
        verbose_name = "Trener mentalny"
        verbose_name_plural = "Trenerzy mentalni"


class Dietitian(Trainer):
    class Meta:
        verbose_name = "Dietetyk"
        verbose_name_plural = "Dietetycy"


class TrainerServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usługa trenera"
        verbose_name_plural = "Usługi trenera personalnego"


class MentalTrainerServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usługa trenera mentalnego"
        verbose_name_plural = "Usługi trenera mentalnego"


class DietitianServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usługa dietetyka"
        verbose_name_plural = "Usługi dietetyków"


class Appointment(BaseModel):
    date = models.DateField()
    hour = models.TimeField()


class TrainerAppointment(Appointment):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    services = models.ForeignKey(TrainerServices, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.services}"

    class Meta:
        verbose_name = "Rezerwacja usługi trenera"
        verbose_name_plural = "Rezerwacja usługi trenera personalnego"


class MentalTrainerAppointment(Appointment):
    trainer = models.ForeignKey(MentalTrainer, on_delete=models.CASCADE)
    services = models.ForeignKey(MentalTrainerServices, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.services}"

    class Meta:
        verbose_name = "Rezerwacja usługi trenera mentalnego"
        verbose_name_plural = "Rezerwacja usługi trenera mentalnego"


class DietitianAppointment(Appointment):
    trainer = models.ForeignKey(Dietitian, on_delete=models.CASCADE)
    services = models.ForeignKey(DietitianServices, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.services}"

    class Meta:
        verbose_name = "Rezerwacja usługi dietetyka"
        verbose_name_plural = "Rezerwacja usługi dietetyka"
