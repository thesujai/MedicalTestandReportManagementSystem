from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import admin,messages
from .models import User,Patient,Doctor, Appointment, Report
from .forms import PatientCreationForm, ReportEntryForm, ReportForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime,timedelta
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    return render(request,'mtrms/index.html')

class LoginDoctor(View):
    template_name='mtrms/login.html'
    context={
        'title':'Doctor Login',
        'action':'mtrms:login_doctor'
    }
    def get(self,request):
        return render(request,self.template_name,self.context)
    
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        
        if user is not None:
            login(request,user)
            doctor=Doctor.objects.get(user=user)
            if doctor:
                request.session['first_name'] = doctor.user.first_name
                url=reverse('mtrms:doctor-dashboard',args=[doctor.user.username])
                return redirect(url)
        return HttpResponse("Not valid ")

class LoginPatient(View):
    template_name='mtrms/login.html'
    context={
        'title':'Patient Login',
        'action':'mtrms:login_patient',
    }
    def get(self,request):
        return render(request,self.template_name,self.context)
    
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        
        if user is not None:
            login(request,user)
            patient=Patient.objects.get(user=user)
            if patient:
                print('user not staff')
                request.session['first_name'] = user.first_name
                url=reverse('mtrms:patient-dashboard',args=[patient.user.username])
                return redirect(url)
        return HttpResponse("Not valid ")

class ChangePassword(View):
    template_name='mtrms/change-password.html'
    context={
        'title':'Change Password',
        'isVerified':False,
    }
    def get(self,request):
        return render(request,self.template_name,self.context)
    
    def post(self,request):
        user=User.objects.filter(username=request.POST.get('username')).exists()
        
        if user:
            print(request)
            request.session['username'] = request.POST.get('username')
            self.context['isVerified']=True
            
            oldPassword=request.POST.get('old-password')
            newPassword=request.POST.get('new-password')
            print(oldPassword,newPassword)
            if oldPassword and newPassword:
                username=request.session.get('username')
                print(username)
                user=User.objects.get(username=username)
                if user.check_password(oldPassword):
                    print('done')
                    user.set_password(newPassword)
                    user.save()
                    return HttpResponse("Successful")
                else:
                    return HttpResponse("Wrong password, please enter correct")
            else:  
                return render(request,self.template_name,self.context)
        else:
            return HttpResponse('No such user exists')
            

class PatientSignup(View):
    template_name='mtrms/signup.html'
    
    def get(self,request):
        form=PatientCreationForm()
        
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=PatientCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            patient=Patient(user=user)
            patient.save()
            return HttpResponse("Success")
        else: 
            print(form.errors)
            return HttpResponse("Invalid")
        
        
def login_patient(request):
    return render(request,'mtrms/login.html')

def signup_patient(request):
    return render(request,'mtrms/signup.html')

def signup_doctor(request):
    return render(request,'mtrms/signup.html')

@login_required(login_url='mtrms:login')
def doctor_dashboard(request,param):
    first_name = request.session.get('first_name', '')
    context={
        'first_name':first_name,
    }
    return render(request,'mtrms/doctor-dashboard.html',context)

@login_required(login_url='mtrms:login')
def patient_dashboard(request,param):
    first_name = request.session.get('first_name', '')
    context={
        'first_name':first_name,
    }
    return render(request,'mtrms/patient-dashboard.html',context)

@method_decorator(login_required, name='dispatch')
class BookAppointment(View):
    
    def get(self,request):
        return render(request,'mtrms/book-appointment.html')

    def post(self, request):
            date = request.POST.get('date')
            time = request.POST.get('time')
            notes = request.POST.get('notes')

            selected_date = datetime.strptime(date, '%Y-%m-%d')
            slots = settings.MORNING_SLOTS if time == 'Morning' else settings.EVENING_SLOTS

            doctors = Doctor.objects.all()
            doctors = doctors.filter(user__is_active=True)
            patient = Patient.objects.get(user=request.user)


            # Iterate through the slots
            for slot_time in slots:
                # Convert the slot time to a datetime object
                slot_start_time = selected_date.replace(
                    hour=int(slot_time[:2]), minute=int(slot_time[3:])
                )
                slot_end_time = slot_start_time + timedelta(minutes=30)

                # Iterate through the doctors to find an available slot
                for doctor in doctors:
                    existing_appointments = Appointment.objects.filter(
                        doctor=doctor,
                        datetime__date=selected_date.date(),
                        datetime__range=(slot_start_time, slot_end_time)
                    )

                    if not existing_appointments.exists():
                        # Slot is available, create the appointment
                        appointment = Appointment(
                            doctor=doctor,
                            patient=patient,
                            datetime=slot_start_time,
                            duration=timedelta(minutes=30),
                            notes=notes
                        )
                        appointment.save()

                        return HttpResponse("success")

            # no slot
            return HttpResponse("No slot available") 

@method_decorator(login_required, name='dispatch')
class ViewAppointments(View):
    def get(self, request):
        doctor = Doctor.objects.get(user=request.user)
        appointments = Appointment.objects.filter(doctor=doctor)
        context = {
            'appointments': appointments,  # Pass the appointments queryset
        }
        return render(request, 'mtrms/view-appointments.html', context)

    def post(self, request):
        if 'mark_done' in request.POST:
            appointment_id = request.POST['appointment_id']
            try:
                appointment = Appointment.objects.get(pk=appointment_id)
                appointment.is_done = True
                appointment.save()
                messages.success(request, f'Appointment for {appointment.patient} marked as done.')
            except Appointment.DoesNotExist:
                messages.error(request, 'Appointment not found.')
        
        elif 'delete_appointment' in request.POST:
            appointment_id = request.POST['appointment_id']
            try:
                appointment = Appointment.objects.get(pk=appointment_id)
                appointment.delete()
                messages.success(request, f'Appointment for {appointment.patient} deleted.')
            except Appointment.DoesNotExist:
                messages.error(request, 'Appointment not found.')

        elif 'input_sample_number' in request.POST:
            appointment_id = request.POST['appointment_id']
            sample_number = request.POST['sample_number']
            try:
                appointment = Appointment.objects.get(pk=appointment_id)
                appointment.sample_number = sample_number
                appointment.save()
                messages.success(request, f'Sample number for {appointment.patient} updated.')
            except Appointment.DoesNotExist:
                messages.error(request, 'Appointment not found.')

        return redirect(reverse('mtrms:view-appointments'))
    
class ReportEntryView(View):
    template_name = 'mtrms/enter-report.html'  # Create this template

    def get(self, request):
        report_form = ReportForm()
        entry_form = ReportEntryForm()
        context = {'report_form': report_form, 'entry_form': entry_form, 'appointment': None}
        return render(request, self.template_name, context)

    def post(self, request):
        entry_form = ReportEntryForm(request.POST)
        if entry_form.is_valid():
            appointment_id = entry_form.cleaned_data['appointment_id']

            try:
                appointment = Appointment.objects.get(id=appointment_id)
            except Appointment.DoesNotExist:
                # Handle case where the appointment ID does not exist
                report_form = ReportForm()
                context = {'report_form': report_form, 'entry_form': entry_form, 'error_message': 'Appointment ID does not exist', 'appointment': None}
                return render(request, self.template_name, context)

            # Pre-fill the form with appointment details
            report_form = ReportForm(initial={'appointment': appointment.id})
            context = {'report_form': report_form, 'entry_form': entry_form, 'appointment': appointment}
            return render(request, self.template_name, context)

        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            # appointment_id = report_form.cleaned_data['appointment_id']
            # appointment = Appointment.objects.get(id=appointment_id)
            # print(request)
            # for x in request:
            #     print(x)
            # print(request.session['apointment_id'])
            # print(appointment)
            # print(entry_form)
            new_report = report_form.save(commit=False)
            # new_report.appointment = appointment
            new_report.date = datetime.now() 
            new_report.save()
        # print(report_form.is_valid())
        context = {'report_form': report_form, 'entry_form': entry_form, 'appointment': None}
        return HttpResponse("Success")   

class PatientAppointmentsView(View):
    template_name = 'mtrms/view-appointments-patient.html'  # Create this template

    def get(self, request):
        # Retrieve the patient's appointments
        appointments = Appointment.objects.filter(patient=request.user.patient)

        context = {'appointments': appointments}
        return render(request, self.template_name, context)
    def post(self, request):
        # Handle actions like marking appointments as done
        appointment_id = request.POST.get('appointment_id')
        mark_done = request.POST.get('mark_done')

        if appointment_id and mark_done:
            # Check if the appointment belongs to the patient
            appointment = Appointment.objects.filter(id=appointment_id, patient=request.user.patient, is_done=False).first()
            if appointment:
                appointment.is_done = True
                appointment.save()

        return redirect('patient-appointments')
def trail(request,param):
    return HttpResponse(f"hi, {param}")