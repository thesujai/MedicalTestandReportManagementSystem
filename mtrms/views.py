from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello i am shaurya")
    return render(request,'mtrms/index.html')

def login_patient(request):
    return render(request,'mtrms/login.html')

def login_doctor(request):
    return render(request,'mtrms/login.html')

def signup_patient(request):
    return render(request,'mtrms/signup.html')

def signup_doctor(request):
    return render(request,'mtrms/signup.html')