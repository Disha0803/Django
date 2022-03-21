from django.db import models
# Create your models here.
class Informations(models.Model):
    info=models.CharField(max_length=20)
    details=models.CharField(max_length=300)
class Informations2(models.Model):
    info2=models.CharField(max_length=20)
    details2=models.CharField(max_length=300)
class Informations3(models.Model):
    info3=models.CharField(max_length=20)
    details3=models.CharField(max_length=300)