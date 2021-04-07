from django.forms import ModelForm, fields
from django import forms
from . models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name','phone_no','email', 'address','time', 'message']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': "form-control", 'name':'your-name', 'placeholder':'Your Name'}),
            'phone_no': forms.TextInput(attrs={'class': "form-control", 'name':'your-phone', 'placeholder':'Your Phone'}),
            'email': forms.TextInput(attrs={'class': "form-control", 'name':'your-email', 'placeholder':'Your Email'}),
            'address': forms.TextInput(attrs={'type':'text','class': "form-control", 'name':'your-address', 'placeholder':'Your Address'}),
            'time': forms.Select(attrs={'class': "form-control", 'name':'your-time'}),
            'message': forms.Textarea(attrs={'class': "form-control", 'name':'your-message', 'placeholder':'Your Message'}),
            
        }