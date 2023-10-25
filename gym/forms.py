from django.utils import timezone

from django import forms

from gym.models import TrainerAppointment, WorkingHour


class TrainerAppointmentForm(forms.ModelForm):
    chosen_hour = forms.ModelChoiceField(
        queryset=WorkingHour.objects.filter(is_available=True),
        empty_label=None,
        widget=forms.Select(attrs={"class": "form-select is_valid"})
    )

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
