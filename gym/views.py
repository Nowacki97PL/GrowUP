from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from gym.forms import TrainerAppointmentForm
from gym.models import TrainerAppointment


class HomeView(TemplateView):
    template_name = 'home.html'


class TrainerAppointmentCreate(CreateView):
    model = TrainerAppointment
    form_class = TrainerAppointmentForm
    template_name = 'create_appointment.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        date = form.cleaned_data['date']
        hour = form.cleaned_data['hour']
        trainer = form.cleaned_data['trainer']

        existing_appointments = TrainerAppointment.objects.filter(
            trainer=trainer,
            date=date,
            hour=hour
        )

        if existing_appointments.exists():
            raise ValidationError("Ten trener ma już rezerwację na tę godzinę w wybranym dniu.")

        if self.request.user.entries > 0:
            form.instance.user = self.request.user
            form.save()

            self.request.user.entries -= 1
            self.request.user.save()

            return super().form_valid(form)
        else:
            form.add_error(None, "Nie masz pakietu treningów. Proszę wykup pakiet.")
            return self.form_invalid(form)
