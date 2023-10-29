from django.urls import path

from gym.views import HomeView, TrainerAppointmentCreate, RentConfirmationView, TrainersList, TrainerDetail

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("create_appointment/", TrainerAppointmentCreate.as_view(), name='create_appointment'),
    path("confirm_reservation/<int:id>/", RentConfirmationView.as_view(), name="confirm_reservation",),
    path('trenerzy/', TrainersList.as_view(), name="trainers"),
    path("trener/<int:pk>/", TrainerDetail.as_view(), name="trainer_detail"),
]
