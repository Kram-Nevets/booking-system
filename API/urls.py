from django.urls import path,include
from .views import UserView,RoomsAPI,RoomDetailsAPI,BookingAPI,RoomImagesAPI,ViewRoomImageAPI,PaymentAPI,PaymentDetailAPI,FeedBackAPI,UserTrackerActivityAPI,CreateUserApi,LogoutView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('bookings',BookingAPI,basename='booking')
router.register('feedback',FeedBackAPI,basename='user_feedback')


urlpatterns = [
    path('users/',UserView.as_view(),name = 'user_view'),
    path('create_users/',CreateUserApi.as_view(),name = 'create_user'),
    path('logout/',LogoutView.as_view(),name = 'api-logout'),
    path('rooms/',RoomsAPI.as_view(),name='rooms'),
    path('rooms/<uuid:uuid>/',RoomDetailsAPI.as_view(),name = 'room_view'),
    path('rooms/room_image/',RoomImagesAPI.as_view(),name = 'RoomImageList'),
    path('rooms/room_image/<uuid:uuid>',ViewRoomImageAPI.as_view(),name = 'Viewroomimage'),
    path('payment/',PaymentAPI.as_view(),name = 'payment'),
    path('payment/<uuid:uuid>',PaymentDetailAPI.as_view(),name = 'payment_detail'),
    path('user_activity/',UserTrackerActivityAPI.as_view(),name = 'useractivity'),
    path('',include(router.urls)),
]
  
