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
    
class Test(models.Model):
    name=models.CharField(max_length=128,blank=False)
    cost=models.IntegerField()
    sample_number=models.IntegerField()
    date=models.DateField()
    
class Report(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.SET_NULL,null=True)
    date=models.DateField()
    result=models.CharField(max_length=128,default='-')
    notes=models.CharField(max_length=10240,blank=True)
    
