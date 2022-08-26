from http.client import HTTPResponse
from logging import RootLogger
from django.shortcuts import render , HttpResponse,redirect
from myapp.models import Dform, Collector,UserRole
from django.contrib.auth.forms import User
from myapp.models import Requestcollector
from datetime import datetime
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import Contributor, Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicespage")

def signup(request):
   if request.method == "POST":
      name = request.POST.get("name") 
      username = request.POST.get("username")
      email =  request.POST.get("email")
      role = request.POST.get("role")
      password = request.POST.get("password")
      confirmpassword = request.POST.get("confirmpassword")
      if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
      if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
      if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
      if password != confirmpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
      if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')  
      myuser = User.objects.create_user(username,email,password)
      myuser.save()
      if role == "Donator":
         signup = Contributor(name = name,email = email,username = username,role = role,password=password)
         signup.save()
         userrole = UserRole(role=role,username=username)
         userrole.save()
      elif role == "Junk Collector":
          signup = Collector(name = name,email = email,username = username,role = role,password=password)
          signup.save()
          userrole = UserRole(role=role,username=username)
          userrole.save()
      messages.success(request,"your account has been successfully created")
      return redirect('signin')
      
   return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if(user is None):
            return redirect(signin)
        else:
            forUserRole = UserRole.objects.get(username = user)
            login(request,user)
            if forUserRole.role=="Junk Collector":
                return redirect(dashboard2)
            else:
                return redirect(dashboard)
    return render(request,"signin.html")

def guidelines(request):
    return render(request,'guidelines.html')

def login2(request):
    return render(request,'login2.html')

def notifications(request):
    return render(request,'notifications.html')

def order_details(request):
    return render(request,'order_details.html')

def notifications2(request):
    return render(request,'notifications2.html')


def dform(request):
    if request.method == "POST":
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        district = request.POST.get('district')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        contact_no = request.POST.get('contact_no')
        date_s = request.POST.get('date_s')
        time = request.POST.get('time')
        ename = request.POST.get('ename')
        quantity = request.POST.get('quantity')
        EwasteType = request.POST.get('EwasteType')
        size = request.POST.get('size')
        weight = request.POST.get('weight')
        e_img = request.POST.get('e_img')
        e_img2 = request.POST.get('e_img2')
        e_img3 = request.POST.get('e_img3')
        dform = Dform(email=email, address1=address1, address2=address2, district=district ,city=city ,state=state ,pincode=pincode ,contact_no=contact_no ,ename=ename, EwasteType = EwasteType, size=size ,quantity=quantity ,date_s=date_s ,time=time, weight=weight, e_img=e_img, e_img2=e_img2, e_img3=e_img3, date=datetime.today())  
        dform.save()
        messages.success(request,"Request sent")
    return render(request,'dform.html')

def requestcollector(request):
        item_list = Dform.objects.all()
        context = {
            'item_list' : item_list
        }
        return render(request,'requestcollector.html',context)

def dashboard3(request):
    return render(request,"dashboard3.html")

def post(request):
    return render(request,"post.html")
   
def profile(request):
    if request.method == "POST":
        address = request.POST.get('address')
        district = request.POST.get('district')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        contact_no = request.POST.get('contact_no')
        profile = Profile(address= address, district=district ,city=city ,state=state ,pincode=pincode ,contact_no=contact_no )  
        profile.save()
        messages.success(request,"Profile Verified")
    return render(request,'profile.html')

#@login_required(login_url='/signin/')
def dashboard(request):
    data= Contributor.objects.get(username = request.user)
    return render(request,'dashboard.html',{'data':data})

def dashboard2(request):
    return render(request,'dashboard2.html')
