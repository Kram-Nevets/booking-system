from django.contrib import admin
from .models import User, Rooms, Booking

# Register your models here.

admin.site.register(User)
admin.site.register(Rooms)
admin.site.register(Booking)
