from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=30)
    ccost=models.FloatField()