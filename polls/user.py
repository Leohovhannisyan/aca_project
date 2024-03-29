from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import PollPatient
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse


def log(request):
    return render(request, 'log_in.html')
def reg(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'GET':
        return render(request, "register.html")

    else:
        first_name = request.POST["name"]
        last_name = request.POST["surname"]
        username = request.POST["username"]
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        PollPatient(user=user).save()

        return render(request,"log_in.html")


def log_in(request):
    if request.method == 'GET':
        return render(request, 'log_in.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            request.session['user_name'] = user.username
            return redirect('doctor_list')

        else:
            return render(request, 'doctor_list.html')

def user_log_out(request):
     if request.method == 'POST':
        logout(request)
        return render(request,'log_in.html')
