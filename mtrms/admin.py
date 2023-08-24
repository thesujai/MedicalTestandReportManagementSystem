from django.contrib import admin
from .models import Doctor,Patient,Test,Appointment,Report

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Test)
admin.site.register(Report)

