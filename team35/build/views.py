from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'build/index.html')
    # return HttpResponse("OK")

def login(request):
    return render(request, 'build/login.html')

def register(request):
    return render(request, 'build/register.html')
    