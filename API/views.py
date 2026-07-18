from rest_framework.views import APIView
from .serializers import UserSerializer, RoomsSerializer, BookingSerializer, PaymentSerializer, FeedbackSerializer, UserActivityTrackingSerializer, RoomImagesSerializer,LogoutSerializer
from admin_side.models import  Rooms, Booking, Payment, Feedback, UserActivityTracking, room_images,User
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.viewsets import ModelViewSet




class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_serializer = UserSerializer(request.user)

        return Response(user_serializer.data)
    

class CreateUserApi(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = LogoutSerializer(data=request.data)

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Successfully logged out"
            }

        )


class RoomsAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class RoomDetailsAPI(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    lookup_field = 'uuid'

class RoomImagesAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = room_images.objects.all()
    serializer_class = RoomImagesSerializer

class ViewRoomImageAPI(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = room_images.objects.all()
    serializer_class = RoomImagesSerializer
    lookup_field = 'uuid'

class BookingAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'uuid'

class PaymentAPI(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailAPI(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'uuid'

class FeedBackAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'uuid'

class UserTrackerActivityAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserActivityTracking.objects.all()
    serializer_class = UserActivityTrackingSerializer








    



    

        
