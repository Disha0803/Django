from django.db import models

# Create your models here.
class Filter(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Email=models.EmailField()
    Course=models.CharField(max_length=30)
    DOB=models.DateField()