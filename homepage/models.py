from django.db import models
from django.utils import timezone


# Create your models here.

class Employee(models.Model):
    e_username=models.CharField(max_length=10, primary_key=True)
    e_password=models.CharField(max_length=10)

class Events(models.Model):
    event_id=models.CharField(max_length=5)
    title=models.CharField(max_length=20)
    start=models.DateTimeField(default=timezone.now)
    end=models.DateTimeField(default=timezone.now)
