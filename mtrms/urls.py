from django.urls import path
from . import views
from .views import LoginDoctor,ChangePassword, LoginPatient, PatientSignup
app_name='mtrms'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/patient',LoginPatient.as_view(),name='login_patient'),
    path('login/doctor',LoginDoctor.as_view(),name='login_doctor'),
    path('signup/patient',PatientSignup.as_view(),name='signup_patient'),
    path('signup/doctor',views.signup_doctor,name='signup_doctor'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor-dashboard'),
    path('patient-dashboard/', views.patient_dashboard, name='patient-dashboard'),
    path('change-password/',ChangePassword.as_view(),name='change-password')
    
]
