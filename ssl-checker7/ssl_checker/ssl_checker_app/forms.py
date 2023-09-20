from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class VideoSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
    clear_search = forms.BooleanField(initial=False, widget=forms.HiddenInput)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'description']