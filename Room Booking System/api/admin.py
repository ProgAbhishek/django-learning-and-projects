from django.contrib import admin
from .models import * #everything
# Register your models here.

admin.site.register(Hotel)
admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Booking)