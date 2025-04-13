from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, MedicalStatus, Appointment, MRIScan, Prescription

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'pincode', 'state']

class MedicalStatusForm(forms.ModelForm):
    class Meta:
        model = MedicalStatus
        fields = ['symptoms', 'current_medication', 'medical_history']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 4}),
            'current_medication': forms.Textarea(attrs={'rows': 4}),
            'medical_history': forms.Textarea(attrs={'rows': 4}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
        }

class MRIScanForm(forms.ModelForm):
    class Meta:
        model = MRIScan
        fields = ['image']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor', 'medication', 'instructions']
        widgets = {
            'medication': forms.Textarea(attrs={'rows': 4}),
            'instructions': forms.Textarea(attrs={'rows': 4}),
        } 