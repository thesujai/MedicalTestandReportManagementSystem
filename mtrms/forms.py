from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Report

User = get_user_model()

class PatientCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'username', 'password1','password2')
        
class ReportEntryForm(forms.Form):
    appointment_id = forms.IntegerField(label='Appointment ID')
    
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['appointment','result', 'notes']