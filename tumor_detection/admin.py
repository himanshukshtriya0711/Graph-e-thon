from django.contrib import admin
from .models import UserProfile, MedicalStatus, Appointment, MRIScan, Prescription

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'pincode', 'state')
    search_fields = ('user__username', 'user__email', 'phone_number')

@admin.register(MedicalStatus)
class MedicalStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'symptoms')
    list_filter = ('date',)
    search_fields = ('user__username', 'symptoms')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'doctor', 'status')
    list_filter = ('date', 'status')
    search_fields = ('user__username', 'doctor')

@admin.register(MRIScan)
class MRIScanAdmin(admin.ModelAdmin):
    list_display = ('user', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('user__username',)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'doctor')
    list_filter = ('date',)
    search_fields = ('user__username', 'doctor', 'medication')
