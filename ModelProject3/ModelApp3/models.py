from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    eaddr=models.CharField(max_length=40)
    esal=models.FloatField()