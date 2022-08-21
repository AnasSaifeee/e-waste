from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse,redirect
from myapp.models import Donor_form
from django.contrib.auth.forms import User
from datetime import datetime
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import extendeduser



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
      aadhaarno = request.POST.get("aadhaarnumber")
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
      signup = extendeduser(name = name,email = email,username = username,aadhaar_no = aadhaarno,password=password)
      signup.save()
     
      messages.success(request,"your account has been successfully created")
      return redirect('signin')
      
   return render(request,"signup.html")

def signin(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      
      user = authenticate(username=username,password=password)
      if user is not None:
         login(request,user)
         return render(request,"dashboard.html")
      else:
         return redirect(signin)
   return render(request,"signin.html")

def guidelines(request):
    return render(request,'guidelines.html')

def login2(request):
    return render(request,'login2.html')

def notifications(request):
    return render(request,'notifications.html')


def donor_form(request):
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
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
        date_s = request.POST.get('date_s')
        time = request.POST.get('time')
        e_img = request.POST.get('e_img')
        donor_form = Donor_form(email=email, address1=address1, address2=address2, district=district ,city=city ,state=state ,pincode=pincode ,contact_no=contact_no ,size=size ,quantity=quantity ,date_s=date_s ,time=time, e_img=e_img, date=datetime.today())  
        donor_form.save()
    return render(request,'donor_form.html')

def dashboard(request):
        return render(request,'dashboard.html')