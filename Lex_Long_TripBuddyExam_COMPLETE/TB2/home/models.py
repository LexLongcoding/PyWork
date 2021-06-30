from django.db import models
from datetime import datetime
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email already in use"

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        
        return errors
    
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw,
        )
        

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    #joined_trips
    #user_trips

    objects = UserManager()

class TripManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['destination']) < 5:
            errors['destination'] = 'Destination field should be at least 5 characters'
        if len(form['description']) < 5:
            errors['description'] = 'Description field should be at least 5 characters'
        if datetime.strptime(form['start_date'], '%Y-%m-%d') < datetime.now():
            errors['start_date'] = 'Start Date should be in the future'
        if datetime.strptime(form['end_date'], '%Y-%m-%d') < datetime.strptime(form['start_date'], '%Y-%m-%d'):
            errors['end_date'] = 'End Date should be after Start Date' 
            return errors
            # 
            #def travels(self, form):
            return self.create(
                destination = form['destination'],
                start_date = form['start_date'],
                end_date = form['end_date'],
                description = form['description']
            )
        

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    trip_creator = models.ForeignKey(User, related_name='user_trips', on_delete=models.CASCADE)
    trip_attendees= models.ManyToManyField(User, related_name='joined_trips')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()