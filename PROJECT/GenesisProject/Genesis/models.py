from django.db import models
event_choice=(
    ('dance','Dance'),
    ('song','Song'),
    ('drama','Drama'),
)
# Create your models here.
class RegistrationForm(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobile=models.BigIntegerField()
    Redgno=models.IntegerField()
    Event=models.CharField(max_length=20,choices=event_choice,default='dance')