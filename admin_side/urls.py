from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('rooms/create/', views.room_create, name='room_create'),
    path('rooms/<int:room_id>/delete/', views.room_delete, name='room_delete'),
]