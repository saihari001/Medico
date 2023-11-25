from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import UploadFiles
from django.http import HttpResponseRedirect
import datetime
from datetime import timedelta

# Create your views here.

def base(request):
    return render(request, "base.html", locals())

def home(request):
    return render(request, "home.html", locals())

def aboutus(request):
    return render(request, "about.html", locals())

def department(request):
    return render(request, "departments.html", locals())

@login_required(login_url="/patientLogIn")
def appointment(request):
    if request.user.is_anonymous:
        messages.warning(request, "Kindly Login to Book Appointment.")
    else:
        u=request.user.email
        print(u)
        obj=Psignup.objects.filter(Email=u)
        obj1=Dsignup.objects.filter(Email=u)
    pfname=request.POST.get('pfname')
    plname=request.POST.get('plname')
    pgender=request.POST.get('pgender')
    page=request.POST.get('page')
    pemail=request.POST.get('pemail')
    pnumber=request.POST.get('pnumber')
    pvisited=request.POST.get('pvisited')
    pspecialist=request.POST.get('pspecialist')
    pappointdate=request.POST.get('pappointdate')
    pappointtime=request.POST.get('pappointtime')
    if request.method=='POST':
        if (Appointment.objects.filter(pappointdate=pappointdate, pappointtime=pappointtime)).exists():
            messages.error(request, "sorry, slot for this timing already booked.")
        else: 
            pappointfetch=Appointment(pfname=pfname, plname=plname, pgender=pgender, page=page, pemail=pemail, pnumber=pnumber, pvisited=pvisited, pspecialist=pspecialist, pappointdate=pappointdate, pappointtime=pappointtime)
            pappointfetch.save()
            messages.success(request, "Thank you, Your Appointment has been Successfully Booked.")

    return render(request, "appointmentform.html", locals())

def contact(request):
    return render(request, "contact.html", locals())

def doctorSignUp(request):
    gfname=request.POST.get("fname")
    glname=request.POST.get("lname")
    ggender=request.POST.get("gender")
    gage=request.POST.get("age")
    gemail=request.POST.get("email")
    gpass=request.POST.get("pass")
    gtandc=request.POST.get("tandc")
    
    #check user name available in database
    dcheck=Dsignup.objects.filter(Email=gemail)
    dcheck1=Psignup.objects.filter(Email=gemail)
    if request.POST:
        if(dcheck and dcheck1):
            messages.error(request, "Already Email Registered.")
        else:
            dstore=Dsignup(FirstName=gfname,LastName=glname,Gender=ggender,Age=gage,Email=gemail,Password=gpass,TandC=gtandc)
            dstore.save()
            user=User.objects.create_user(gemail,gemail,gpass)
            user.save()
            messages.success(request, "You have been successfully registered.")
            return redirect(doctorLogIn)
    else:
        w=""
    return render(request, "docsignup.html", locals())

def doctorLogIn(request):
    if request.POST:
        vemail=request.POST.get("email")
        vpass=request.POST.get("pword")
        user=authenticate(username=vemail, password=vpass)   
        #vcheck=Dsignup.objects.filter(Email=vemail,Password=vpass)
        if (user!=None):
            if(user.is_authenticated):
                login(request, user)
                return redirect(home)
            else:
                messages.error(request, "invalid user")
        else:
            messages.error(request, "Pls Enter Valid Email and Password")
            
    return render(request, "doclogin.html", locals())
    
def logout_profile(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect(doctorLogIn)

def patientSignUp(request):
    gfname=request.POST.get("fname")
    glname=request.POST.get("lname")
    ggender=request.POST.get("gender")
    gage=request.POST.get("age")
    gemail=request.POST.get("email")
    gpass=request.POST.get("pass")
    gtandc=request.POST.get("tandc")
    
    #check user name available in database
    dcheck=Psignup.objects.filter(Email=gemail)
    dcheck1=Dsignup.objects.filter(Email=gemail)

    if request.method == 'POST':
        if(dcheck and dcheck1):
            w="Email already registered"
        else:
            dstore=Psignup(FirstName=gfname,LastName=glname,Gender=ggender,Age=gage,Email=gemail,Password=gpass,TandC=gtandc)
            dstore.save()
            user=User.objects.create_user(gemail,gemail,gpass)
            user.save()
            w="Successfully Registered"
            return redirect(patientLogIn)
    else:
        w=" "
    return render(request, "patientsignup.html", locals())

def patientLogIn(request):
    #vcheck=Psignup.objects.filter(Email=vemail,Password=vpass)
    if(request.method=='POST'):
        vemail=request.POST.get("email")
        vpass=request.POST.get("pass")
        user=authenticate(username=vemail, password=vpass)
        if(user!=None):
            if(user.is_authenticated):
                login(request, user)
                messages.success(request, "you have been successfully logged in")
                return redirect(home)
            else:
                messages.error(request, "invalid user")
        else:
            messages.error(request, "Enter corrrect username and password")
    return render(request, "patientlogin.html", locals())

def profile(request):
    if(request.user):
        u=request.user.email
        print(u)
        obj=Dsignup.objects.filter(Email=u)
        obj1=Psignup.objects.filter(Email=u)
        if obj:
            data=obj
            print(obj)
        else:
            data=obj1
            print(obj1)
            
    return render(request, "profile.html", locals())

def edit(request, id):
    if(request.user):
        u=request.user.email
        print(u)
        obj=Dsignup.objects.filter(Email=u)
        obj1=Psignup.objects.filter(Email=u)
        if obj:
            gi=Dsignup.objects.get(pk = id)
        elif obj1:
            gi=Psignup.objects.get(pk = id)
    if request.method == 'POST':
        gi.FirstName=request.POST.get("fname")
        gi.LastName=request.POST.get("lname")
        gi.save()
        return redirect(profile)
    else:
        print("error")
    return render(request, "profile.html", locals())

# def singlepage(request):
#     pages={
#         "Ent":"First_Page",
#         "Medical":"Second_Page",
#         "Cardiac":"https://www.google.co.in/"
#     }
#     context={
#         "data":pages
#     }
#     return render(request, "single.html", locals())

# def images(request):
#     obj=ImageGallery.objects.all()
#     k=len(obj)
#     return render(request, "imgform.html", locals())

# def upload_file(request):
#     if request.method == 'POST':
#         form=UploadFiles(request.POST, request.FILES)
#         if(form.is_valid()):
#             form.save()
#             img_obj=form.instance
#             return render(request, "upload.html", locals())
#     else:
#         form=UploadFiles()
#         return render(request, "upload.html", locals())

# def cards(request):
#     obj1=ImageGallery.objects.all()
#     return render(request, "cards.html", locals())

# def appoint(request):
#     if request.user:
#         u=request.user
#         print(u)
#         if request.method == 'POST':
#             pname=request.POST.get("pname")
#             pgender=request.POST.get("gender")
#             if request.POST.get("astatus"):
#                 st=request.POST.get("astatus")
#                 pappoint=Appoint.objects.filter(pname=pname)
#                 pappoint['pname']=pname
#                 pappoint['gender']=pgender
#                 pappoint['astatus']=st
#                 pappoint.save()
#             else:
#                 pappoint=Appoint(pname=pname, gender=pgender)
#                 pappoint.save()
#         else:
#             print("Enter valid Details")
#     else:
#         print("user not na")
#     return render(request, "appoint.html", locals())

@login_required(login_url='/patientLogIn')
def myappointments(request):
    if request.user:
        u=request.user.email
        print(u)
        obj=Psignup.objects.filter(Email=u)
        if obj:
            data=Appointment.objects.filter(pemail=u)
            if request.method=='POST':
                appoint=request.POST.get("bid")
                print(appoint)
                return redirect("myappointments/"+appoint)
        else:
            return redirect(consultation)
    return render(request, "myappointments.html", locals())

def getappointments(request, id=None):
    if id is not None:
        data=Appointment.objects.filter(bid=id)
        print('id',id)
    return render(request, "myappointments.html", locals())


@login_required(login_url='/doctorLogIn')
def consultation(request):
    if request.user:
        u=request.user.email
        print(u)
        obj=Dsignup.objects.filter(Email=u)
        if obj:
            data=Appointment.objects.all()
        else:
            return redirect(myappointments)
    return render(request, "consultation.html", locals())

def editconsultation(request, id):
    gid=Appointment.objects.get(pk=id)
    print(gid)
    if request.method == 'POST':
        gid.pappointdate=request.POST.get('pappointdate')
        gid.pappointtime=request.POST.get('pappointtime')
        gid.pstatus=request.POST.get('pstatus')
        gid.pprescription=request.POST.get('pprescription')
        gid.save()
    return render(request, "consultation.html", locals())
        
    
        
        
            

# def consultation(request, id):
#     gid=Appoint.objects.get(pk = id)
#     if request.user:
#         u=request.user
#         print(u)
#         if request.method == 'POST':
#             pname=request.POST.get("pname")
#             pgender=request.POST.get("gender")
#             if request.POST.get("astatus"):
#                 st=request.POST.get("astatus")
#                 print(st)
#                 pappoint=Appoint.objects.get(pname=pname)
#                 print(pappoint," hello ")
#                 pappoint.pname=pname
#                 pappoint.gender=pgender
#                 pappoint.astatus=st
#                 pappoint.save()
#                 return redirect(consult)
#         else:
#             print("Enter valid Details")
#     else:
#         print("user not na")
#     return render(request, "appoint.html", locals())
    
    
def timing(request):
    dt=datetime.datetime(2023,10,28,10,00,0)
    print(dt)
    dt1=datetime.datetime(2023,10,28,12,00,0)
    dt2=datetime.timedelta(minutes=10)
    print(dt2)
    while(dt<=dt1):
        print(dt.strftime('%H:%M'), end="\n")
        dt+=dt2
        
        
    # dt2=dt1.strftime('%H:%M')
    # print(dt2)
    return render(request, "timing.html", locals())

def medicine(request):
    return render(request, "medicine.html", locals())

def rating(request, id):
    gid=Appointment.objects.get(pk=id)
    name=gid.pfname
    bid=gid.bid
    rev=Review.objects.filter(pk=id)
    rname=rev[0].name
    # print(list(rev.values()))
    print("Rating received ",rev[0].rating)
    rateno=rev[0].rating
    col={1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
    ratecol=col[rateno]
    rate=range(rev[0].rating)
    
    if request.method == 'POST':
        rate=request.POST.get("ratee")
        cmt=request.POST.get("comment")
        rfetch=Review(name=name, bid=bid, rating=rate, comment=cmt)
        rfetch.save()
        print(rfetch)
        return redirect(myappointments)
    return render(request, "rating.html", locals())

def searchdb(request):
    if request.method=='POST':
        query=request.POST.get("query")
        print(query)
        return redirect("search/"+query)
    return render(request, "searchbar.html", locals())

def analyzesearchdb(request, id=None):
    query=request.POST.get("query")
    print(query)
    print(id)
    if id is not None:
        ap=Appointment.objects.filter(bid=id)
    return render(request, "searchbar.html", locals())

def newsearch(request):
    if request.method == 'POST':
        srh=request.POST["search"]
        # appoint=Appointment.objects.filter(pfname__icontains=srh)
        appoint=Appointment.objects.filter(pfname=srh, bid=srh)

    return render(request, "newsearch.html", locals())