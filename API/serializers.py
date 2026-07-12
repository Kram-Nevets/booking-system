from rest_framework import serializers
from admin_side.models import User, Rooms, Booking, Payment, Feedback, UserActivityTracking, room_images



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','phone_number','email','role','is_active','created_at','updated_at']

        read_only_fields = ['created_at','updated_at']

class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = room_images
        fields = ['image']

class RoomsSerializer(serializers.ModelSerializer):

    images = RoomImagesSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Rooms
        fields = ['uuid','room_number','room_name','room_type','room_status','capacity','images','price_per_night','is_available','description','created_at','updated_at',]

        read_only_fields = ['uuid','created_at','updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['uuid','user','room','checkin','checkout','number_of_guests','total_price','booking_status','created_at','updated_at']
        read_only_fields = ['uuid','created_at','updated_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['uuid','booking','payment_method','amount','payment_status','created_at','updated_at']
        read_only_fields = ['uuid','created_at','updated_at']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['uuid','user','room','comment','rating','created_at','updated_at']
        read_only_fields = ['uuid','created_at','updated_at']

class UserActivityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivityTracking
        fields = ['uuid','user','activity_type','activity_description','timestamp']
        read_only_fields = ['uuid','timestamp']