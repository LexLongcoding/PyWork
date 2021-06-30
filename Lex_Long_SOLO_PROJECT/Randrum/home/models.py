from django.db import models
from datetime import datetime
import re, bcrypt


EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')
class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['username']) < 2:
            errors['username'] = 'First Name must be at least 2 characters'
        
        username_check = self.filter(username=form['username'])
        if username_check:
            errors['username'] = "Username already in use"

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
            username = form['username'],
            email = form['email'],
            password = pw,
        )
        
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    #created_kits
    #favorited_kits

    objects = UserManager()

class KitManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['title']) < 2:
            errors['title'] = 'Title must be at least 2 characters'
            return errors
            return self.create()


class Kit(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    kick = models.CharField(max_length=255)
    snare = models.CharField(max_length=255)
    HHcl = models.CharField(max_length=255)
    HHop = models.CharField(max_length=255)
    crash = models.CharField(max_length=255)
    ride = models.CharField(max_length=255)
    tom_h = models.CharField(max_length=255)
    tom_m = models.CharField(max_length=255)
    tom_l = models.CharField(max_length=255)
    perc = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='created_kits', on_delete=models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name='favorited_kits')
    objects = KitManager()