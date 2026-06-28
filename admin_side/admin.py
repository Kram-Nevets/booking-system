from django.contrib import admin
from .models import User, Rooms, Booking,room_images

# Register your models here.

admin.site.register(User)
admin.site.register(Rooms)
admin.site.register(Booking)
admin.site.register(room_images)
