from django import forms
from django.utils import timezone
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import TrainerAppointment, MentalTrainerAppointment, DietitianAppointment
from .widgets import FullHourSelect


class TrainerAppointmentForm(forms.ModelForm):
    hour = forms.ChoiceField(choices=[], widget=FullHourSelect(attrs={'class': 'form-control is_valid'}))

    class Meta:
        model = TrainerAppointment
        fields = "__all__"
        widgets = {
            "trainer": forms.Select(attrs={"class": "form-select is_valid"}),
            "date": forms.DateInput(attrs={"class": "form-control is_valid", "type": "date"}),
            "services": forms.Select(attrs={"class": "form-select is_valid"}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        today = timezone.now().date()
        if date < today:
            raise forms.ValidationError("Niepoprawna data. Wybierz właściwą datę.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        trainer = cleaned_data.get('trainer')

        existing_appointments = TrainerAppointment.objects.filter(
            trainer=trainer,
            date=date,
            hour=hour
        )

        if existing_appointments.exists():
            raise forms.ValidationError("Ten trener ma już rezerwację na tę godzinę w wybranym dniu.")

    def __init__(self, *args, **kwargs):
        super(TrainerAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['hour'].choices = self.get_hour_choices()

    def get_hour_choices(self):
        return [(str(i), f"{i}:00") for i in range(7, 24)]


class MentalTrainerAppointmentForm(forms.ModelForm):
    hour = forms.ChoiceField(choices=[], widget=FullHourSelect(attrs={'class': 'form-control is_valid'}))

    class Meta:
        model = MentalTrainerAppointment
        fields = "__all__"
        widgets = {
            "trainer": forms.Select(attrs={"class": "form-select is_valid"}),
            "date": forms.DateInput(attrs={"class": "form-control is_valid", "type": "date"}),
            "services": forms.Select(attrs={"class": "form-select is_valid"}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        today = timezone.now().date()
        if date < today:
            raise forms.ValidationError("Niepoprawna data. Wybierz właściwą datę.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        trainer = cleaned_data.get('trainer')

        existing_appointments = MentalTrainerAppointment.objects.filter(
            trainer=trainer,
            date=date,
            hour=hour
        )

        if existing_appointments.exists():
            raise forms.ValidationError("Ten trener ma już rezerwację na tę godzinę w wybranym dniu.")

    def __init__(self, *args, **kwargs):
        super(MentalTrainerAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['hour'].choices = self.get_hour_choices()

    def get_hour_choices(self):
        return [(str(i), f"{i}:00") for i in range(7, 24)]


class DietitianAppointmentForm(forms.ModelForm):
    hour = forms.ChoiceField(choices=[], widget=FullHourSelect(attrs={'class': 'form-control is_valid'}))

    class Meta:
        model = DietitianAppointment
        fields = "__all__"
        widgets = {
            "trainer": forms.Select(attrs={"class": "form-select is_valid"}),
            "date": forms.DateInput(attrs={"class": "form-control is_valid", "type": "date"}),
            "services": forms.Select(attrs={"class": "form-select is_valid"}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        today = timezone.now().date()
        if date < today:
            raise forms.ValidationError("Niepoprawna data. Wybierz właściwą datę.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        trainer = cleaned_data.get('trainer')

        existing_appointments = DietitianAppointment.objects.filter(
            trainer=trainer,
            date=date,
            hour=hour
        )

        if existing_appointments.exists():
            raise forms.ValidationError("Ten trener ma już rezerwację na tę godzinę w wybranym dniu.")

    def __init__(self, *args, **kwargs):
        super(DietitianAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['hour'].choices = self.get_hour_choices()

    def get_hour_choices(self):
        return [(str(i), f"{i}:00") for i in range(7, 24)]


