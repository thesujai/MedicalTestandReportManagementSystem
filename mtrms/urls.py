from django.urls import path
from . import views
from .views import LoginDoctor,login_patient,signup_doctor,signup_patient
app_name='mtrms'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/patient',views.login_patient,name='login_patient'),
    path('login/doctor',LoginDoctor.as_view(),name='login_doctor'),
    path('signup/patient',views.signup_patient,name='signup_patient'),
    path('signup/doctor',views.signup_doctor,name='signup_doctor'),
    
]
