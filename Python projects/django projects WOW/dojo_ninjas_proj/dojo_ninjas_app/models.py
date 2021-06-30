from django.db import models


class Ninja(models.Model):
    #id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Dojo(models.Model):
#id
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(max_length=255)
    Ninja = models.ForeignKey(Dojo, related_name="ninja", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def name(self):
        return f"{self.first_name}{self.last_name}"


# Create your models here