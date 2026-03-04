from django.shortcuts import render

from rest_framework import generics
from .models import Location, Hotel, Room
from .serializers import LocationSerializer, HotelSerializer, RoomSerializer

#create location api
class CreateLocationAPIView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
 
#2 apis, create and list 
class ListCreateHotelAPIView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

#3 different apis
class RoomAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "pk"
