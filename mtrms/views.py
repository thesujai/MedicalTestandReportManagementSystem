from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import admin
from .models import User,Patient
from .forms import PatientCreationForm

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
            if user.is_staff:
                request.session['first_name'] = user.first_name
                return redirect('/doctor-dashboard/')
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
            print("User exists")
            if not user.is_staff:
                print('user not staff')
                request.session['first_name'] = user.first_name
                return redirect('/patient-dashboard/')
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


def doctor_dashboard(request):
    first_name = request.session.get('first_name', '')
    context={
        'first_name':first_name,
    }
    return render(request,'mtrms/doctor-dashboard.html',context)

def patient_dashboard(request):
    first_name = request.session.get('first_name', '')
    context={
        'first_name':first_name,
    }
    return render(request,'mtrms/patient-dashboard.html',context)