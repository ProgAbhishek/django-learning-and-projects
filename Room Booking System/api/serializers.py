from rest_framework.serializers import ModelSerializer
from .models import Location, Hotel , Room

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
        fields = "__all__"
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"