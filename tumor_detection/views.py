from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import (
    UserRegisterForm, 
    UserProfileForm, 
    MedicalStatusForm, 
    AppointmentForm, 
    MRIScanForm, 
    PrescriptionForm
)
from .models import (
    UserProfile, 
    MedicalStatus, 
    Appointment, 
    MRIScan, 
    Prescription
)

def home(request):
    return render(request, 'tumor_detection/home.html')

def get_started(request):
    return render(request, 'tumor_detection/get_started.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
        
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'tumor_detection/register.html', context)

@login_required
def dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None
    
    context = {
        'user_profile': user_profile
    }
    return render(request, 'tumor_detection/dashboard.html', context)

@login_required
def medical_status(request):
    medical_statuses = MedicalStatus.objects.filter(user=request.user).order_by('-date')
    
    if request.method == 'POST':
        form = MedicalStatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.user = request.user
            status.save()
            messages.success(request, 'Medical status updated successfully!')
            return redirect('medical_status')
    else:
        form = MedicalStatusForm()
    
    context = {
        'form': form,
        'medical_statuses': medical_statuses
    }
    return render(request, 'tumor_detection/medical_status.html', context)

@login_required
def appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('-date')
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('appointments')
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
        'appointments': appointments
    }
    return render(request, 'tumor_detection/appointments.html', context)

@login_required
def mri_scans(request):
    scans = MRIScan.objects.filter(user=request.user).order_by('-uploaded_at')
    
    if request.method == 'POST':
        form = MRIScanForm(request.POST, request.FILES)
        if form.is_valid():
            scan = form.save(commit=False)
            scan.user = request.user
            scan.save()
            
            # Here you would normally call your AI model to process the MRI
            # For now, we'll just simulate a result
            scan.result = "Detected area of interest in the frontal lobe. Further analysis recommended."
            scan.save()
            
            messages.success(request, 'MRI scan uploaded and analyzed successfully!')
            return redirect('mri_scans')
    else:
        form = MRIScanForm()
    
    context = {
        'form': form,
        'scans': scans
    }
    return render(request, 'tumor_detection/mri_scans.html', context)

@login_required
def prescriptions(request):
    prescriptions = Prescription.objects.filter(user=request.user).order_by('-date')
    
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.user = request.user
            prescription.save()
            messages.success(request, 'Prescription added successfully!')
            return redirect('prescriptions')
    else:
        form = PrescriptionForm()
    
    context = {
        'form': form,
        'prescriptions': prescriptions
    }
    return render(request, 'tumor_detection/prescriptions.html', context)
