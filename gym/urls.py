from django.urls import path

from gym.views import HomeView, TrainerAppointmentCreate, RentConfirmationView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("create_appointment/", TrainerAppointmentCreate.as_view(), name='create_appointment'),
    path("confirm_reservation/<int:id>/", RentConfirmationView.as_view(), name="confirm_reservation",),
]
