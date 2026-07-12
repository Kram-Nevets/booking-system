from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from cloudinary.models import CloudinaryField



class User(AbstractUser):
   
   CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
   uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   phone_number = models.CharField(max_length=15)
   email = models.EmailField(unique=True)
   role = models.CharField(max_length=20, choices=CHOICES, default='customer')
   is_active = models.BooleanField(default=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
        return self.username




class Rooms(models.Model):
    ROOM_TYPE_CHOICES = (
            ('single', 'Single'),
            ('double', 'Double'),
            ('suite', 'Suite'),
        )
    ROOM_STATUS_CHOICES = (
        ('available', 'Available'),
        ('occupied', 'Occupied'), 
        ('unavailable', 'Unavailable'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    room_number = models.IntegerField()
    room_name = models.CharField(max_length=50,null=True,blank=True)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    room_status = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room  {self.id}  {self.room_number} - {self.room_name}"


class room_images(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image',folder='room_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image {self.id} - Room {self.room.room_number}"

    

class Booking(models.Model):

    BOOKING_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )


    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.uuid} - {self.user.username} - Room {self.room.room_number}"

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

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.uuid} - {self.booking}"

class Feedback(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback {self.uuid} - {self.user.username} - Room {self.room.room_number}"

class UserActivityTracking(models.Model):

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    activity_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity {self.uuid} - {self.user.username} - {self.activity_type}"






