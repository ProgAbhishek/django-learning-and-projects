from django.urls import path
from .views import CreateLocationAPIView, ListCreateHotelAPIView, RoomAPIView

urlpatterns = [
    path('Create-location',CreateLocationAPIView.as_view() ),
    path('List-Create',ListCreateHotelAPIView.as_view() ),
    path('room/<int:pk>',RoomAPIView.as_view())
]
