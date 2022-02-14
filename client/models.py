from django.db import models

# Create your models here.

class Client(models.Model): # Client is the name of the table in the database

    fullname = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=16, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)