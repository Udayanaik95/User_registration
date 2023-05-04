from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from django.core.mail import send_mail

# Create your views here.

def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUFO=UFD.save(commit=False)
            NSUFO.set_password(UFD.cleaned_data['password'])
            NSUFO.save()

            NSPFO=PFD.save(commit=False) 
            NSPFO.username=NSUFO
            NSPFO.save()

            send_mail('Registration','Registration Successfully Done','Udayanaik95@gmail.com',[NSUFO.email],fail_silently=False)

            return HttpResponse('User Registration Successfull')
        else:
            return HttpResponse('Data Is Not Valid')

    return render(request,'registration.html',d)

# fail_silently=False use to know the error, if any Error is there