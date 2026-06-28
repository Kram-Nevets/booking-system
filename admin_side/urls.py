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
    path('rooms/<int:room_id>/update/', views.room_update, name='room_update'),
    path('users/', views.user_list, name='user_list'), 
    path('settings/', views.settings, name='settings'),
    path('room_images/', views.Images, name='room_images'),
    path('room_images/upload_images',views.image_upload,name='room_image_upload'),
    path('rooms/media/<int:image_id>/delete/', views.delete_image,name='room_image_delete'),
]