from django.shortcuts import render, HttpResponse, redirect
from .models import user, travel
from django.contrib import messages

def index(request):
    context={
        "user": user.objects.all()
    }
   
    return render(request, "travelapp/login.html", context)

def logout(request):
    request.session.clear()
    return render(request, "travelapp/logout.html")
   

def reg(request):
    errors=user.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')

    else:
        fn = request.POST['Fname']
        ln = request.POST['Lname']
        em = request.POST['Email']
        pa = request.POST['Password']
        us=user.objects.create(Fname=fn, Lname=ln, Email=em, Password=pa)
        request.session['user'] = us.id
        return redirect('/dashboard')

def login(request):
    errors=user.objects.sec_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    em = request.POST['Email']
    ruser=user.objects.get(Email=em)
    pa = request.POST['Password']
    if ruser.Password == pa:
        request.session['user'] = ruser.id
        return redirect('/dashboard')
    else:
        return redirect('/')
    
def dashboard(request):
    us = user.objects.get( id = request.session['user'])

    context={
        "travel": us.travels.all()
    }
    request.session['user']
    return render(request, "travelapp/dashboard.html", context)

def create(request):
    context={
        "travel": travel.objects.all()
    }

    return render(request, "travelapp/newtrip.html", context)

def add_trip(request):
    errors=travel.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/create')

    dDestination = request.POST['Destination']
    sStartdate = request.POST['Start_date']
    eEnddate = request.POST['End_date']
    pPlan = request.POST['Plan']
    t=travel.objects.create(Destination=dDestination,Start_date=sStartdate,End_date=eEnddate,Plan=pPlan) 
    us = user.objects.get( id = request.session['user'])
    t.users.add(us)

    return redirect('/dashboard')   

def details(request, num):
    context = {
        "ts": travel.objects.get(id=num)
    }
    return render(request, "travelapp/index4.html", context)
    request.session['user']
def destroy(request, num):

    travel.objects.get(id=num).delete()

    return redirect('/dashboard')

def edittrip(request, num):
    context={
        "travel": travel.objects.get(id=num)
    }
    request.session['user']
    return render(request, "travelapp/editit.html", context)

def edittemp(request, num):
    errors = travel.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edittrip/'+num)
    else:    
        qr = travel.objects.get(id=num)
        qr.Destination = request.POST['Destination']
        qr.Start_date = request.POST['Start_date']
        qr.End_date = request.POST['End_date']
        qr.Plan = request.POST['Plan']
        qr.save()
        return redirect(f'/details/{num}') 
