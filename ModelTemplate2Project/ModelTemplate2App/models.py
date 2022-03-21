from django.db import models
# Create your models here.
class Classical_Dance_Forms(models.Model):
    dname=models.CharField(max_length=30)
    dorigin=models.CharField(max_length=30)
    dcost=models.FloatField()
class Modern_Dance(models.Model):
    mname=models.CharField(max_length=30)
    morigin=models.CharField(max_length=30)
    mcost=models.FloatField()
