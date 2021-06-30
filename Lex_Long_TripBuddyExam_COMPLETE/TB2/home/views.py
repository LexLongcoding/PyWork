from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trip, User
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/travels')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "Welcome")
    return redirect('/travels')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, '/travels', context)

def new(request):
    return render(request, 'addtrip.html')

def trip(request, trip_id):
    
    one_trip = Trip.objects.get(id=trip_id)
    context = {
        'trip': one_trip
    }
    return render(request, 'view.html', context)



def create(request):

    errors = Trip.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
    else:
        trip = Trip.objects.create(
            destination = request.POST['destination'],
            description = request.POST['description'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            trip_creator = User.objects.get(id=request.session['user_id'])
        )
        trip.save()
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    user_trips = Trip.objects.filter(trip_creator=user.id)
    other_trips = Trip.objects.exclude(trip_creator=user.id)
    context = {
        'user': user,
        "trips": user_trips,
        "other_trips": other_trips
        
    }
    return render(request, 'travels.html', context)


def delete(request, trip_id):

    to_delete = Trip.objects.get(id=trip_id)
    to_delete.delete()
    return redirect('/travels')


def travels(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    user_trips = Trip.objects.filter(trip_creator_id=user.id)
    other_trips = Trip.objects.exclude(trip_creator_id=user.id)
    context = {
        'user': user,
        "trips": user_trips,
        "other_trips": other_trips,
        "all_trips": Trip.objects.all()
    }
    return render(request, 'travels.html', context)

def view(request, trip_id):
    context = {
        "trip":Trip.objects.get(id=trip_id),
        #"user": User.objects.get(id=trip_creator)
    }
    return render(request, 'view.html', context)

def join_trip(request, id):
    user_joining = User.objects.get(id=request.session['user_id'])
    this_trip=Trip.objects.get(id=id)
    this_trip.trip_attendees.add(user_joining)
    
    
    return redirect('/travels')

def cancel_trip(request, id):
    user_canceling = User.objects.get(id=request.session['user_id'])
    this_trip=Trip.objects.get(id=id)
    this_trip.trip_attendees.remove(user_canceling)
    

    #to_cancel = Trip.objects.get(id=trip_id)
    
    return redirect('/travels')



# Create your views here.
