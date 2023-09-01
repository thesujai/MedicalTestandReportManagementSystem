from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import LoginDoctor,ChangePassword, LoginPatient, PatientSignup
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
    path('book-appointment/',views.book_appointment,name='book-appointment'),
    
]
