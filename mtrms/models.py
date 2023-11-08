from django.db import models

from django.contrib import admin

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    datetime=models.DateTimeField()
    duration=models.DurationField()
    notes=models.CharField(max_length=10240,blank=True)
    is_done = models.BooleanField(default=False)
    sample_number = models.PositiveIntegerField(null=True, blank=True,default=None)
    def __str__(self):
        return f"{self.id}"

    
class Report(models.Model):
    appointment=models.ForeignKey(Appointment,on_delete=models.SET_NULL,null=True)
    date=models.DateField()
    result=models.CharField(max_length=128,default='-')
    notes=models.CharField(max_length=10240,blank=True)
    def __str__(self):
        return f"{self.id}"
    
