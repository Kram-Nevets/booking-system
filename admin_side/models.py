from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
   
   CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
   uuid = models.UUIDField(unique=True, editable=False, null=True, blank=True)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   phone_number = models.CharField(max_length=15)
   email = models.EmailField(unique=True)
   role = models.CharField(max_length=20, choices=CHOICES)
   is_active = models.BooleanField(default=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)



class Rooms(models.Model):
    ROOM_TYPE_CHOICES = (
            ('single', 'Single'),
            ('double', 'Double'),
            ('suite', 'Suite'),
        )
    ROOM_STATUS_CHOICES = (
        ('available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )

    uuid = models.UUIDField(unique=True, editable=False)
    room_number = models.IntegerField()
    room_name = models.CharField(max_length=50,null=True,blank=True)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    room_status = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField()
    description = models.TextField()
    room_image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

class Booking(models.Model):

    BOOKING_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )


    uuid = models.UUIDField(unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )

    uuid = models.UUIDField(unique=True, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    uuid = models.UUIDField(unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserActivityTracking(models.Model):

    uuid = models.UUIDField(unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    activity_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)






