from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from datetime import datetime

from numpy import imag
from home.models import Contact ,Event, Profile,Eventlogin
from home.models import Register
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login

from datetime import date


from .models import *

global eventreg
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")



def about(request):
    return render(request, 'about.html') 

def logout(request):
    return render(request, 'login.html')

def services(request):
    return render(request, 'services.html')

def profile(request):
    if request.method == "POST":
        profilename = request.POST.get('profilename')
        profileemail = request.POST.get('profileemail')
        profilenumber = request.POST.get('profilenumber')
        branch = request.POST.get('branch')
        
        profiledesc = request.POST.get('profiledesc')
        profileimage = request.FILES['profileimage']
        profiledetail = Profile(profilename = profilename,profileemail = profileemail,profilenumber = profilenumber,branch = branch,profiledesc = profiledesc,profileimage = profileimage)
        profiledetail.save()
        messages.success(request, 'Profile detail saved !!')
        return redirect('/forms')
    else:
        return render(request,'profile.html')


def forms(request):
    return render(request, 'forms.html') 

def register(request):
    #print(request.method)
    if request.method == "POST":
        
        name1 = request.POST['name1']
        username = request.POST['username']
       # print[email]
        
        password = request.POST['password']
        #printpassword)

        password2 = request.POST['password2']
        if password == password2 :
            if User.objects.filter(username = username).exists():
                messages.info(request,'Email already exist')
                return redirect('/register')
            else :
                user = User.objects.create_user(username,username,password)
                user.save()
                messages.info(request,'Registered Succesfully')
                return redirect('/login')
        # return redirect('/login')
        # messages.success(request, 'You have registered succesfully.'
        else:
            messages.info(request,'Incorrect Password')
            return redirect('/profile')
    else:
        return render(request, 'register.html') 
    

    # return render(request, 'register.html',{'form':form})
 
def login(request):
    if request.method == "POST":
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
        #print(loginemail)
        #print(loginpassword) 
        user = authenticate(username = loginemail,password = loginpassword)
        #print(user)
        if user is not None:
            #print(2)
            messages.info(request,'Succesfully logged in')
             
            auth.login(request,user)
            return redirect ('/forms')
        else:
           # print(1)
            messages.info(request,'Invalid Login')
            return redirect('/login')
    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect("/")


def contact(request):
    print(request.method)
    if request.method == "POST":
        print(1)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def events(request):
    if request.method == "POST":
        clubname = request.POST.get('clubname')
        eventname = request.POST.get('eventname')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        eventdetail = Event(clubname = clubname,eventname = eventname,date = date,desc = desc,image = image)
        eventdetail.save()
        messages.success(request, 'Event detail saved !!')
        return redirect('/forms')
    else:
        return render(request,'events.html')

def allevents(request):
    if request.method == "POST":
         club_name = request.POST.get('clubname')
         club_name_upper = club_name.upper()
         events = Event.objects.filter(clubname=club_name_upper)
         context={"events":events}
         return render(request,'allevents.html',context)
    events=Event.objects.order_by("-date")
    context={"events":events}
    return render(request,'allevents.html',context)


def allprofiles(request):
    
    if request.method == "POST":
         branch_name = request.POST.get('branchname')
         branch_name_upper = branch_name.upper()
         profiles = Profile.objects.filter(branch=branch_name_upper)
         context={"profiles":profiles}
         return render(request,'allprofiles.html',context)
    profiles=Profile.objects.all()
    context={"profiles":profiles}
    return render(request,'allprofiles.html',context)
    

def eventlogin(request):
        # print("request = ",eventreg) 
        
        global eventreg
        if request.method == "POST":
            # eventreg = eventreg.GET['eventname1'] 
            print("Inside")
            studentname = request.POST.get('studentname') 
            collegeemail = request.POST.get('collegeemail') 
            mis = request.POST.get('mis') 
            branch = request.POST.get('branch') 
            mobile = request.POST.get('mobile') 
            event = Eventlogin(studentname= studentname,collegeemail = collegeemail,mis = mis,branch = branch,mobile = mobile,eventreg=eventreg)
            event.save() 
            print(eventreg)
            messages.success(request, 'Detail saved !!')
            return redirect('/allevents')
        else:
            #print("Here")
            eventreg=request.GET['eventname1']
            #print(eventreg)
            return render(request,'eventlogin.html')    

        

def allregistrations(request):
    
    if request.method == "POST":
         event_name = request.POST.get('eventname')
         eventlogins = Eventlogin.objects.filter(eventreg=event_name)
         context={"eventlogins":eventlogins}
         return render(request,'allregistrations.html',context)
    eventlogins=Eventlogin.objects.all()
    context={"eventlogins":eventlogins}
    return render(request,'allregistrations.html',context)