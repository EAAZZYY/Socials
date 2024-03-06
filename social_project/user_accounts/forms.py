from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username",'email',"password1","password2"]
        labels = {
            "username":"Nickname",
            "password1":"Enter Password",
            "password":"Confirm Password"
        }
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["profile_pic","first_name","last_name","hobbies","about_you"]