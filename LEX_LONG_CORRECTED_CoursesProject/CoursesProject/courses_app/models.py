from django.db import models
from datetime import datetime

class CourseManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['course_name']) < 6:
            errors['course_name'] = 'Course name must be more than 5 characters'
        if len(form['course_description']) < 16:
            errors['course_description'] = 'Course description must be more than 15 characters'
        
        return errors

class Description(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)

    objects = CourseManager()



# Create your models here.
