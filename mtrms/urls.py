from django.urls import path
from django.shortcuts import HttpResponse
from django.contrib.auth import views as auth_views
from . import views
from .views import LoginDoctor,ChangePassword, LoginPatient, PatientSignup, BookAppointment,ViewAppointments, ReportEntryView, PatientAppointmentsView
app_name='mtrms'
urlpatterns = [
    path('',views.index,name='index'),
    path('accounts/login/', views.index, name='login'),
    path('login/patient',LoginPatient.as_view(),name='login_patient'),
    path('login/doctor',LoginDoctor.as_view(),name='login_doctor'),
    path('signup/patient',PatientSignup.as_view(),name='signup_patient'),
    path('signup/doctor',views.signup_doctor,name='signup_doctor'),
    path('doctor/<str:param>/', views.doctor_dashboard, name='doctor-dashboard'),
    path('patient/<str:param>/', views.patient_dashboard, name='patient-dashboard'),
    path('change-password/',ChangePassword.as_view(),name='change-password'),
    path('book-appointment/',BookAppointment.as_view(),name='book-appointment'),
    path('appointments/',ViewAppointments.as_view(),name='view-appointments'),
    path('create-report/<int:appointment_id>/',views.trail,name='create-report'),
    path('enter-report/', ReportEntryView.as_view(), name='enter-report'),
    path('appointments-patient/',PatientAppointmentsView.as_view(),name='appointments-patient')
]
