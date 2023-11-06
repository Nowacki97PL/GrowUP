from django.urls import path

from gym.views import HomeView, TrainerAppointmentCreate, RentConfirmationView, TrainersList, TrainerDetail, \
    MentalTrainerAppointmentCreate, DietitianAppointmentCreate, ChooseSpecialistView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("choose_specialist/", ChooseSpecialistView.as_view(), name='choose_specialist'),
    path("create_appointment/", TrainerAppointmentCreate.as_view(), name='create_appointment'),
    path("create_mental-trainer_appointment/", MentalTrainerAppointmentCreate.as_view(), name='create_mental_trainer_appointment'),
    path("create_dietitian_appointment/", DietitianAppointmentCreate.as_view(), name='create_dietitian_appointment'),
    path("confirm_reservation/<int:id>/", RentConfirmationView.as_view(), name="confirm_reservation",),
    path('trenerzy/', TrainersList.as_view(), name="trainers"),
    path("trener/<int:pk>/", TrainerDetail.as_view(), name="trainer_detail"),
]
