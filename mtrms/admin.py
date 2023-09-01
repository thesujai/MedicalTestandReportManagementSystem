from django.contrib import admin
from .models import Doctor,Patient,Test,Appointment,Report,User
from django.contrib.auth.hashers import make_password

# Register your models here.
# admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Test)
admin.site.register(Report)
class CustomUserAdmins(admin.ModelAdmin):
    actions = ['set_hashed_password']
    list_display=('id','username')
    
    def set_hashed_password(self, request, queryset):
        # Replace 'password123' with the desired password
        newPassword = User.objects.make_random_password()
        print(f"New Password:{newPassword}")
        hashedPassword = make_password(newPassword)
        queryset.update(password=hashedPassword)
        self.message_user(request, "Passwords updated and hashed.")
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
