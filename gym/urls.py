from django.urls import path

from gym.views import HomeView, TrainerAppointmentCreate

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("create_appointment/", TrainerAppointmentCreate.as_view(), name='create_appointment'),
]
