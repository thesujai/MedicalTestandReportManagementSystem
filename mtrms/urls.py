from django.urls import path
from . import views
from .views import LoginDoctor,ChangePassword, LoginPatient
app_name='mtrms'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/patient',LoginPatient.as_view(),name='login_patient'),
    path('login/doctor',LoginDoctor.as_view(),name='login_doctor'),
    path('signup/patient',views.signup_patient,name='signup_patient'),
    path('signup/doctor',views.signup_doctor,name='signup_doctor'),
    path('doctor-dashboard/', views.dashboard, name='doctor-dashboard'),
    path('change-password/',ChangePassword.as_view(),name='change-password')
    
]
