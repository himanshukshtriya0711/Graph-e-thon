from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username

class MedicalStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    symptoms = models.TextField()
    current_medication = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Medical Status on {self.date}"

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.user.username}'s Appointment on {self.date} at {self.time}"

class MRIScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='mri_scans/')
    result = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s MRI Scan on {self.uploaded_at}"

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    doctor = models.CharField(max_length=100)
    medication = models.TextField()
    instructions = models.TextField()
    
    def __str__(self):
        return f"{self.user.username}'s Prescription on {self.date}"
