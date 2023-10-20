from django import forms

from gym.models import TrainerAppointment


class TrainerAppointmentForm(forms.ModelForm):
    class Meta:
        model = TrainerAppointment
        fields = "__all__"
        widgets = {
            "trainer": forms.Select(attrs={"class": "form-select is_valid"}),
            "date": forms.DateInput(
                attrs={"class": "form-control is_valid", "type": "date"}
            ),
            "hour": forms.Select(attrs={"class": "form-select is_valid"}),
            "services": forms.Select(attrs={"class": "form-select is_valid"}),
        }
