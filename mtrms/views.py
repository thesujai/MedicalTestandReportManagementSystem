from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    # return HttpResponse("Hello i am shaurya")
    return render(request,'mtrms/index.html')

class LoginDoctor(View):
    template_name='mtrms/login.html'
    context={
        'title':'Doctor Login',
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
                print("Hello")
                login(request, user)
                request.session['first_name'] = user.first_name
                return redirect('/doctor-dashboard/')
        return HttpResponse("Not valid ")
    
def login_patient(request):
    return render(request,'mtrms/patient.html')

def signup_patient(request):
    return render(request,'mtrms/signup.html')

def signup_doctor(request):
    return render(request,'mtrms/signup.html')



def dashboard(request):
    first_name = request.session.get('first_name', '')
    context={
        'first_name':first_name,
    }
    return render(request,'mtrms/doctor-dashboard.html',context)
    # return HttpResponse("Welcome")