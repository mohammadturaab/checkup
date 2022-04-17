from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)

    class Meta:
        models = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
