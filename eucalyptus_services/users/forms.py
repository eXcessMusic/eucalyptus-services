from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.conf import settings
import os

class CustomUserCreationForm(UserCreationForm):
    invite_code = forms.CharField(max_length=50, required=True, help_text="Enter the invite code you received.")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "invite_code")

    def clean_invite_code(self):
        invite_code = self.cleaned_data.get('invite_code')
        expected_code = os.environ.get('REGISTRATION_INVITE_CODE')
        
        if not expected_code:
            raise ValidationError("Registration is currently not available.")
        
        if invite_code != expected_code:
            raise ValidationError("Invalid invite code.")
        
        return invite_code

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username  = forms.CharField(max_length=100)
    password  = forms.CharField(max_length=100, widget=forms.PasswordInput)