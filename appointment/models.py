from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.first_name},{self.last_name}"
class Appointments(models.Model):
    user=models.ForeignKey(Person,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return f"{self.user},{self.date},{self.time}"