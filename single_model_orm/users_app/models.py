from django.db import models

class users(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email_address = models.TextField(Max_length=255)
    age = models.IntegerField(45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
