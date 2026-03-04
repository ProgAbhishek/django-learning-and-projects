from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return f"{self.city}--{self.state}"

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    total_rooms = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}--{self.location} -- {self.total_rooms}"

class Room(models.Model):
    capacity = models.IntegerField(default=1)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null = True)