from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/patient',views.login_patient,name='login_patient'),
    path('login/doctor',views.login_doctor,name='login_doctor'),
    path('signup/patient',views.signup_patient,name='signup_patient'),
    path('signup/doctor',views.signup_doctor,name='signup_doctor'),
    
]
