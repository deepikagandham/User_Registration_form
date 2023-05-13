from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.core.mail import send_mail

# from django.http import HttpResponseRedirect
# from django.contrib.auth import authenticate,login,logout
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required

# def home(request):

#     if request.session.get('username'):
#         username=request.session.get('username')
#         d={'username':username}
#         return render(request,'home.html',d)
    

#     return render(request,'home.html')



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
                    fail_silently=True )

            return HttpResponse('Registration is done')
        else:
            return HttpResponse('Not Valid')
    return render(request,'registration.html',d)
# def user_login(request):

#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         AUO=authenticate(username=username,password=password)
#         if AUO and AUO.is_active:
#             login(request,AUO)
#             request.session['username']=username
#             return HttpResponseRedirect(reverse('home'))
#         else:
#             return HttpResponse('Invalid username or password') 
        
#     return render(request,'user_login.html')
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('home'))

# def f_w(request):
#     if request.method=='POST':
#         un=request.POST['un']
#         pw=request.POST['pw']

#         LUO=User.objects.filters(username=un)
#         if LUO:
#             UO=LUO[0]
#             UO.set_password[pw]
#             UO.save()
#             return HttpResponse('password reset is done')
#         else:
#             return HttpResponse('username is not available in DB')
#     return render(request,'f_w.html')


