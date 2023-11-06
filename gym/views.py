from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from gym.forms import TrainerAppointmentForm, MentalTrainerAppointmentForm, DietitianAppointmentForm
from gym.models import TrainerAppointment, Trainer, MentalTrainerAppointment, DietitianAppointment


class HomeView(TemplateView):
    template_name = 'home.html'


class TrainerAppointmentCreate(CreateView):
    model = TrainerAppointment
    form_class = TrainerAppointmentForm
    template_name = 'create_appointment.html'
    success_url = reverse_lazy("confirm_reservation", kwargs={"id": 0})

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
            reservation = form.save()
            self.success_url = reverse_lazy("confirm_reservation", kwargs={"id": reservation.id})

            self.request.user.entries -= 1
            self.request.user.save()

            return super().form_valid(form)
        else:
            form.add_error(None, "Nie masz pakietu treningów. Proszę wykup pakiet.")
            return self.form_invalid(form)


class MentalTrainerAppointmentCreate(CreateView):
    model = MentalTrainerAppointment
    form_class = MentalTrainerAppointmentForm
    template_name = 'create_appointment.html'
    success_url = reverse_lazy("confirm_reservation", kwargs={"id": 0})


class DietitianAppointmentCreate(CreateView):
    model = DietitianAppointment
    form_class = DietitianAppointmentForm
    template_name = 'create_appointment.html'
    success_url = reverse_lazy("confirm_reservation", kwargs={"id": 0})


class RentConfirmationView(TemplateView):
    template_name = "confirm_reservation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservation_id = self.kwargs.get("id")
        reservation = TrainerAppointment.objects.get(pk=reservation_id)
        context["reservation"] = reservation
        return context


class ChooseSpecialistView(TemplateView):
    template_name = 'choose_specialist.html'

    def post(self, request, *args, **kwargs):
        specialist_choice = request.POST.get('specialist_choice')

        if specialist_choice == '1':
            return reverse_lazy('create_appointment')
        elif specialist_choice == '2':
            return reverse_lazy('create_mental-trainer_appointment')
        elif specialist_choice == '3':
            return reverse_lazy('create_dietitian_appointment')
        else:
            # Obsłuż sytuację, gdy wybór jest nieprawidłowy
            return self.render_to_response({'error': 'Nieprawidłowy wybór'})


class TrainersList(ListView):
    model = Trainer
    template_name = 'trainer_list.html'
    context_object_name = 'trainers'


class TrainerDetail(DetailView):
    model = Trainer
    template_name = 'trainer_detail.html'
