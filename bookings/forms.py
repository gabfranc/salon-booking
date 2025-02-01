from django import forms
from .models import Booking  # Import your Booking model

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time', 'name', 'email', 'phone'] # Fields from your model
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }