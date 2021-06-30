from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    # CREATE THE COURSE
    errors = Course.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
    
    else:
        course = Course.objects.create(
            name = request.POST['course_name'],
            description =request.POST['course_description']
        )
        #Description.objects.create(content=request.POST['desc'])
        #course.description = desc
        course.save() 

    return redirect("/")   

def delete(request,id):
    if request.method == "GET":
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request,'delete.html', context)

    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
        return redirect("/courses")
