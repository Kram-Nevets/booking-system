from time import timezone
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  UserLoginForm, RoomForm , UploadRoomImageForm
from .models import User, Rooms, Booking, Payment, Feedback, UserActivityTracking, room_images




def user_login(request):

    if request.method == 'POST':
         
        user_form = UserLoginForm(request, data=request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
    
    else:
        user_form = UserLoginForm()

    return render(request, 'user_auth_forms/admin_login.html', {'form': user_form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):

    total_bookings = Booking.objects.select_related('user', 'room').all()
    total_users = User.objects.count()
    total_rooms = Rooms.objects.count()
    total_bookings = Booking.objects.count()
    upcoming_bookings = Booking.objects.filter(booking_status='pending').count()
    cancelled_bookings = Booking.objects.filter(booking_status='cancelled').count()
    occupied_rooms = Rooms.objects.filter(room_status='occupied').count()
    available_rooms = Rooms.objects.filter(room_status='available').count()
    cancelled_bookings = Booking.objects.filter(booking_status='cancelled').count()
    pending_bookings = Booking.objects.filter(booking_status='pending').count()
    available_rooms = Rooms.objects.filter(room_status='available').count()
    rooms_unavailable = Rooms.objects.filter(room_status='Unavailable').count()

    
    return render(request, 'admin_templates/dashboard.html', {
        'bookings': total_bookings,
        'total_users': total_users,
        'total_rooms': total_rooms,
        'total_bookings': total_bookings,
        'upcoming_bookings': upcoming_bookings,
        'cancelled_bookings': cancelled_bookings,
        'occupied_rooms': occupied_rooms,
        'available_rooms': available_rooms,
        'cancelled_bookings': cancelled_bookings,
        'pending_bookings': pending_bookings,
        'available_rooms': available_rooms,
        'rooms_unavailable': rooms_unavailable,

    })


@login_required
def rooms_list(request):
    rooms = Rooms.objects.all()
    return render(request, 'admin_templates/rooms.html', {'rooms': rooms})


@login_required
def booking_list(request):
    bookings = Booking.objects.select_related('user', 'room').all()
    return render(request, 'admin_templates/bookings.html', {'bookings': bookings})

@login_required
def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms_list')
            
    else:
        form = RoomForm()

        print(form.errors)
    
    return render(request, 'admin_templates/room_form.html', {'form': form})

@login_required
def room_delete(request, room_id):
    room = Rooms.objects.get(id=room_id)
    room.delete()
    return redirect('rooms_list')

@login_required
def room_update(request, room_id):
    room = Rooms.objects.get(id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'admin_templates/room_form.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'admin_templates/users.html', {'users': users})

@login_required
def settings(request):
    return render(request, 'admin_templates/settings.html')

@login_required
def Images(request):
    RoomImages = room_images.objects.select_related('room').all()
    return render(request, 'admin_templates/room_images.html', {'room_images': RoomImages}) 

@login_required
def image_upload(request):

    room = Rooms.objects.all()
    if request.method == "POST":
        form = UploadRoomImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('room_images')
        
    else:
        form = UploadRoomImageForm()

    return render(request,'admin_templates/room_image_upload.html',{
            'room':room,
            'form':form,
        })

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(room_images, id=image_id)
    image.delete()
    return redirect('room_images')
   