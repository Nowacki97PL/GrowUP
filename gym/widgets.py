from django import forms


class FullHourSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        super(FullHourSelect, self).__init__(*args, **kwargs)
        self.choices = [(str(i), f"{i}:00") for i in range(0, 24)]
