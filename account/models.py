from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Checkin(models.Model):
    room = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email=models.EmailField()
    occupation=models.CharField(max_length=100)
    night=models.CharField(max_length=10)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    staff=models.ForeignKey(User, on_delete=models.CASCADE)
    time_checkedin=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name