from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
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
        return redirect('/wall')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    #messages.success(request, "You have successfully logged in!")
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')

'''def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)'''

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'wall_messages': Wall_Post.objects.all()

    }
    return render(request, 'wall.html', context)

def new_post(request):
    Wall_Post.objects.create(message=request.POST['message'], poster=User.objects.get(id=request.session['user_id']))
    return redirect('/wall')

def new_comment(request, id):
    poster = User.objects.get(id=request.session['user_id'])
    message = Wall_Post.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/wall')

def delete_comment(request, id):
    destroyed = Comment.objects.get(id=id)
    destroyed.delete()
    return redirect('/wall')

def profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def add_like(request, id):
    liked_message = Wall_Post.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/wall')
