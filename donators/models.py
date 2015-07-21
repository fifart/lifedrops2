from django.db import models

# Create your models here.

class Donator(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    slug = models.SlugField(unique=True)
    blood_types_choices = (('A+','A+'), ('A-','A-'), ('B+','B+'),('B-', 'B-'), ('AB+','AB+'),('AB-','AB-'),('0+','O+'),('0-','O-'))
    blood_type = models.CharField(max_length=4, choices=blood_types_choices, default='A+')
    registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)