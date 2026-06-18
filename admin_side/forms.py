from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User, Rooms, Booking


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

