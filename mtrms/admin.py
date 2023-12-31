from django.contrib import admin
from .models import Doctor,Patient,Appointment,Report,User
from django.contrib.auth.hashers import make_password

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Report)
class CustomUserAdmins(admin.ModelAdmin):
    actions = ['set_hashed_password']
    list_display=('id','username')
    
    def set_hashed_password(self, request, queryset):
        for user in queryset:
            newPassword=f"{user.username}"
            hashedPassword = make_password(newPassword)
            user.password=hashedPassword
            user.save()
            self.message_user(request, "Passwords updated and hashed.\nNew password: <username>")
    set_hashed_password.short_description = "Set hashed password for selected users"
    
admin.site.register(User,CustomUserAdmins)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username',)

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username' 
admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username',)

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username' 
admin.site.register(Doctor, DoctorAdmin)
