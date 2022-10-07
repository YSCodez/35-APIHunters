from django.shortcuts import render
from django.shortcuts import  redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, get_user

# Create your views here.
def homepage(request):
    return render(request, 'build/index.html')
    #return HttpResponse("OK")

def login(request):
    return render(request, 'build/login.html')

def register(request):
    return render(request, 'build/register.html')

def editprofile(request):
    return render(request, 'build/editprofile.html')

def UserRegister(request):
    if request.method == 'POST':
        #Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        passwd = request.POST['passwd']
        cpasswd= request.POST['cpasswd']

        #Check for errorinput

        if not username.isalnum():
            messages.error(request, "Username should contain only letters and numbers!!")
            return redirect('/')

        #Create User
        myuser = User.objects.create_user(username, email, passwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Timescale account was created successfully!!")
        return redirect('/')
    else:
        messages.error(request, "Request method is not post")
        return redirect('/')

def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid Credentials, Please try again!!")
            return redirect('/')

def profile(request):
    return render(request, 'build/editprofile.html')

def resume(request):
    return render(request, 'build/srt-resume.html')
