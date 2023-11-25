from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class Dsignup(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Gender=models.CharField(max_length=10)
    Age=models.CharField(max_length=3)
    Email=models.CharField(max_length=40)
    Password=models.CharField(max_length=20)
    TandC=models.CharField(max_length=10)
    def __str__(self):
        return self.Email +", "+ self.FirstName 

class Psignup(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Gender=models.CharField(max_length=10)
    Age=models.CharField(max_length=3)
    Email=models.CharField(max_length=40)
    Password=models.CharField(max_length=20)
    TandC=models.CharField(max_length=10)
    def __str__(self):
        return self.Email +", "+ self.FirstName 

class ImageGallery(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
    video=models.FileField(upload_to='videos', blank=True)
    def __str__(self):
        return self.title   
    
class Appoint(models.Model):
    pname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    astatus=models.CharField(max_length=30, default="Pending")

class Appointment(models.Model):
    bid=ShortUUIDField(length=4, max_length=4, alphabet="1234567890", primary_key=True, null=False)
    pfname=models.CharField(max_length=40)
    plname=models.CharField(max_length=40)
    pgender=models.CharField(max_length=10)
    page=models.IntegerField()
    pemail=models.CharField(max_length=100)
    pnumber=models.IntegerField()
    pvisited=models.CharField(max_length=4)
    pspecialist=models.CharField(max_length=30)
    pappointdate=models.DateField()
    pappointtime=models.TimeField()
    pstatus=models.CharField(max_length=30, default="Pending")
    pprescription=models.FileField(null=True, blank=True, upload_to='prescription')
    def __str__(self):
        return " Booking ID: "+self.bid+"  "+"Name: "+self.pfname+" "+self.plname
    
class Review(models.Model):
    name=models.CharField(blank=True, null=True, max_length=50)
    bid=models.IntegerField(blank=True, primary_key=True)
    rating=models.IntegerField(blank=True, null=True)
    comment=models.TextField(blank=True, null=True)   