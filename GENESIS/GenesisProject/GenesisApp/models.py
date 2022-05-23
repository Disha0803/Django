from django.db import models
events=(
    ('Dance','Dance'),
    ('Song','Song'),
    ('Drama','Drama'),
)
# Create your models here.
class Registration(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Mobile=models.BigIntegerField()
    Redgno=models.IntegerField()
    Event=models.CharField(max_length=20,choices=events,default='Song')