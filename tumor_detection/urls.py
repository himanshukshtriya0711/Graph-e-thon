from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-started/', views.get_started, name='get_started'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tumor_detection/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tumor_detection/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('medical-status/', views.medical_status, name='medical_status'),
    path('appointments/', views.appointments, name='appointments'),
    path('mri-scans/', views.mri_scans, name='mri_scans'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
] 