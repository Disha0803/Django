from django.db import models

# Create your models here.
class StudentForm(models.Model):
    Name=models.CharField(max_length=30)
    Redg_No=models.IntegerField()
    Age=models.IntegerField()
    Email=models.EmailField()
    Phn_No=models.IntegerField()