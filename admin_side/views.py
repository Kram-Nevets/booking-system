from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from .models import User, Rooms, Booking


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_auth_forms/register.html', {'form': form})


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
    queryset = Booking.objects.all()
    return render(request, 'admin_templates/dashboard.html', {'bookings': queryset})






