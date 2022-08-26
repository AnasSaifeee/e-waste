import imp
from math import degrees
from pydoc import render_doc
from django.db import models
from django.contrib.auth.forms import User

class UserRole(models.Model):
     username = models.CharField(max_length = 20,null = True)
     role= models.CharField(max_length=20, null = True)
     def __str__(self):
        return self.username
class Contributor(models.Model):
     name = models.CharField(max_length=20)
     role= models.CharField(max_length=20, null = True)
     email =  models.CharField(max_length = 12,null= True)
     password = models.CharField(max_length = 20,null = True)
     username = models.CharField(max_length = 20,null = True)
     def __str__(self):
        return self.username

class Dform(models.Model):
    email =models.CharField(max_length = 122)
    address1=models.CharField(max_length= 122)
    address2 = models.CharField(max_length = 122)
    district = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    pincode = models.CharField(max_length = 122)
    contact_no =models.CharField(max_length = 12)
    ename=models.CharField(max_length=122)
    EwasteType = models.CharField(max_length =122)
    size = models.CharField(max_length = 122)
    weight = models.CharField(max_length=122)
    quantity = models.CharField(max_length = 122)
    date_s = models.CharField(max_length = 122)
    time = models.CharField(max_length = 122)
    e_img = models.FileField(upload_to='', storage=None, max_length=100)
    e_img2 = models.FileField(upload_to='', storage=None, max_length=100)
    e_img3 = models.FileField(upload_to='', storage=None, max_length=100)
    date = models.DateField()

class Requestcollector(models.Model):
    email =models.CharField(max_length = 122)
    address1=models.CharField(max_length= 122)
    address2 = models.CharField(max_length = 122)
    district = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    pincode = models.CharField(max_length = 122)
    contact_no =models.CharField(max_length = 12)
    ename=models.CharField(max_length=122)
    EwasteType = models.CharField(max_length =122)
    size = models.CharField(max_length = 122)
    weight = models.CharField(max_length=122)
    quantity = models.CharField(max_length = 122)
    date_s = models.CharField(max_length = 122)
    time = models.CharField(max_length = 122)
    e_img = models.FileField(upload_to='', storage=None, max_length=100)
    e_img2 = models.FileField(upload_to='', storage=None, max_length=100)
    e_img3 = models.FileField(upload_to='', storage=None, max_length=100)

class Profile(models.Model):
    address=models.CharField(max_length= 122)
    district = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    pincode = models.CharField(max_length = 122)
    contact_no =models.CharField(max_length = 12)
    def __str__(self):
        return self.pincode

class Events(models.Model):
    coordinator_name = models.CharField(max_length=122)
    coordinator_phone = models.IntegerField()
    coordinator_email = models.CharField(max_length = 122)
    event_name = models.CharField(max_length = 122)
    event_desc = models.CharField(max_length = 122)
    venue = models.CharField(max_length = 122)
    event_date = models.CharField(max_length = 122)
    time = models.CharField(max_length = 122)
    
# class Donator(models.Model):
#     Donator_Id = models.IntegerField(primary_key=True,null=False)
#     Name = models.CharField(max_length = 100)
#     Contact_No = models.CharField(max_length = 20)
#     Address = models.CharField(max_length = 100)
#     Email = models.CharField(max_length = 50)
#     Don_location = models.CharField(max_length = 100)
#     Ver_Prrof = models.IntegerField()
#     Ewaste_Id = models.ForeignKey()
    
# class Collector(models.Model):
#     JC_Id = models.IntegerField(primary_key=True,null=False)
#     JC_Name = models.CharField(max_length = 100)
#     Contact_No = models.CharField(max_length = 20)
#     Address = models.CharField(max_length = 100)
#     Email = models.CharField(max_length = 50)
#     JC_Location = models.CharField(max_length = 100)
#     Ver_Proof =  models.IntegerField()
#     Vehicle = models.CharField(max_length = 100)
#     Ewaste_Id = models.ForeignKey()

# class Dealer(models.Model):
#     JD_Id =  models.IntegerField(primary_key=True,null=False)
#     DC_Name = models.CharField(max_length = 100)
#     Contact_No = models.CharField(max_length = 20)
#     Address = models.CharField(max_length = 100)
#     Email = models.CharField(max_length = 50)
#     JD_Location = models.CharField(max_length = 100)
#     Ver_Proof =  models.IntegerField()
#     Vehicle = models.CharField(max_length = 100)
#     Location_Shop = models.CharField(max_length = 100)
#     Shop_Regno = models.CharField(max_length = 100)
#     Ewaste_Id = models.ForeignKey()

# class Recycle_Plant(models.Model):
#     RP_Id =  models.IntegerField(primary_key=True,null=False)
#     JC_Name =  models.CharField(max_length = 100)
#     Contact_no =  models.CharField(max_length = 100)
#     Adress =  models.CharField(max_length = 100)
#     Email =  models.CharField(max_length = 100)
#     JC_Location =  models.CharField(max_length = 100)
#     Ver_Proof = models.IntegerField()
#     Vehicle =  models.CharField(max_length = 100)
#     Location =  models.CharField(max_length = 100)

# class Ewaste(models.Model):
#     Ewaste_Id = models.IntegerField(primary_key=True,null=False)
#     Name = models.CharField(max_length = 100)
#     Dimensions = models.CharField(max_length = 100)
#     Type = models.CharField(max_length = 100)
#     Size = models.CharField(max_length = 100)
#     Weight = models.CharField(max_length = 100)
#     Donator_Id =models.ForeignKey()
#     JC_Id =models.ForeignKey()
#     Booking_Id =models.ForeignKey()
#     JD_Id = models.ForeignKey()
#     RP_Id = models.ForeignKey()
#     Status = models.CharField(max_length = 20)

# class Pickup_Booking(models.Model):
#      Booking_Id =  models.IntegerField(primary_key=True,null=False)
#      Pickup_location = models.CharField(max_length = 100)
#      Ewaste_Id = models.ForeignKey()
#      Booking_Status =  models.CharField(max_length = 20)
#      Startof_pickup = models.CharField(max_length = 100)
#      Endof_Pickup = models.CharField(max_length = 100)
