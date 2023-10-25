from django.db import models
from accounts.models import UserProfile, MyUser
from gym.choices import type_job, working_hours


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WorkingHour(models.Model):
    time = models.CharField(max_length=10, unique=True, null=True)
    is_available = models.BooleanField(default=True)

    def reserve_hour(self):
        if self.is_available:
            self.is_available = False
            self.save()

    def __str__(self):
        return self.time


class Trainer(BaseModel):
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=32, choices=type_job)
    working_hours = models.ManyToManyField(WorkingHour, related_name='trainers', null=True)

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


class TrainerServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class MentalTrainerServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price} zł"


class DieticianServices(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price} zł"


class Appointment(BaseModel):
    date = models.DateField()
    chosen_hour = models.ForeignKey(WorkingHour, on_delete=models.CASCADE, null=True)


class TrainerAppointment(Appointment):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    services = models.ForeignKey(TrainerServices, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.services}"


class MentalTrainerAppointment(Appointment):
    trainer = models.ForeignKey(MentalTrainer, on_delete=models.CASCADE)
    services = models.ForeignKey(MentalTrainerServices, on_delete=models.CASCADE)


class DieticianAppointment(Appointment):
    trainer = models.ForeignKey(Dietician, on_delete=models.CASCADE)
    services = models.ForeignKey(DieticianServices, on_delete=models.CASCADE)
