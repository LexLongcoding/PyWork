from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
import bcrypt


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
        return redirect('/dashboard')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "Welcome")
    return redirect('/dashboard')

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
    return render(request, '/dashboard', context)

def new(request):
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'user': user,
    }
    
    return render(request, 'addwish.html', context)

def wish(request, wish_id):
    
    one_wish = Wish.objects.get(id=wish_id)
    context = {
        'wish': one_wish
    }
    return render(request, 'edit.html', context)

def create(request):

    errors = Wish.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/addwish')
    else:
        wish = Wish.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            wish_creator = User.objects.get(id=request.session['user_id'])
        )
        wish.save()
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    user_wishes = Wish.objects.filter(wish_creator=user.id)
    other_wishes = Wish.objects.exclude(wish_creator=user.id)
    context = {
        "user": user,
        "wishes": user_wishes,
        "other_wishes": other_wishes,
        
        
    }
    return redirect('/dashboard')

def delete(request, wish_id):

    to_delete = Wish.objects.get(id=wish_id)
    to_delete.delete()
    return redirect('/dashboard')


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    all_users = User.objects.all()
    user_wishes = Wish.objects.filter(wish_creator_id=user.id)
    other_wishes = Wish.objects.exclude(wish_creator_id=user.id)
    other_users = User.objects.exclude(id=user.id)
    all_wishes = Wish.objects.all()

    context = {
        'user': user,
        'all_users': all_users,
        "wishes": user_wishes,
        "other_wishes": other_wishes,
        "all_wishes": all_wishes,
        "other_users": other_users
        
        
    }
    return render(request, 'dashboard.html', context)

def edit(request, wish_id):
    context = {
        "wish":Wish.objects.get(id=wish_id),
        #"user": User.objects.get(id=trip_creator)
    }
    return render(request, 'edit.html', context)

def update(request,  id):
    update_wish = Wish.objects.get(id=id)
    update_wish.title = request.POST['title']
    update_wish.description = request.POST['description']
    update_wish.save()

    return redirect('/dashboard')
    
def grant_wish(request, id):
    user_granting = User.objects.get(id=request.session['user_id'])
    this_wish=Wish.objects.get(id=id)
    user_granting.granted_wishes.add(this_wish)
    
    return redirect('/dashboard')
    
    


# Create your views here.
