from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.core.mail import send_mail
def registration(request):
    UFD=UserForm()
    PFD=ProfileForm()
    d={'UFD':UFD,'PFD':PFD}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            Password=UFD.cleaned_data['password']
            NSUO.set_password(Password)
            NSUO.save()

            NSPO=PFD.save(commit=False)
            NSPO.Username=NSUO
            NSPO.save()
            send_mail('Registration',
                      'Succesfully Registration is done',
                      'deepikagandham5@gmail.com',
                      [NSUO.email],
                      fail_silently=False )

            return HttpResponse('Registration is done')
        else:
            return HttpResponse('Not Valid')
    return render(request,'registration.html',d)