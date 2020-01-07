from django.db import models

# Create your models here.
class Student(models.Model):
    
    fname = models.TextField(max_length = 40)
    lname = models.TextField()
    department = models.TextField()