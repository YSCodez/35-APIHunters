
from django.shortcuts import render
from django.shortcuts import  redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, get_user

from build.models import personaldet

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
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        passwd = request.POST['pass']
        cpasswd= request.POST['pass2']

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

def personaldetail(request):
    if request.method == 'POST':
      if request.POST.get('email')  :
        personal=personaldet()
        personal.email = request.POST['email']
        personal.graduateyear = request.POST['graduate']
        personal.percentage = request.POST['percentage']
        personal.yearofgraduation = request.POST['yearofgraduation']
        personal.skills= request.POST['skills']
        personal.interested_sub= request.POST['interestedsub']
        personal.save()
        messages.success(request,'Record saved')
        return redirect('/login/')
    return redirect('/login.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'build/editprofile.html')
    else:
        return redirect('/')

def resume(request):
    return render(request, 'build/srt-resume.html')

def handleuserLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!!')
    return render(request, 'build/logout.html')