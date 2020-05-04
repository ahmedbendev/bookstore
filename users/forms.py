from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Client,Publisher

class UserForm(UserCreationForm):

        class Meta:
          model = User
          fields = ["username","email","password1","password2"]

class UserUpdateForm(forms.ModelForm):
      email = forms.EmailField()

      class Meta:
        model = User
        fields = ['username','email']

class ProfileForm(forms.ModelForm):
      class Meta :
        model = Profile
        fields = ['image','type']

class ProfileUpdateForm(forms.ModelForm):
      class Meta:
        model = Profile
        fields = ['image']

class ClientinfoUpdateForm(forms.ModelForm):

      class Meta:
        model = Client
        fields = ['first_name_cl','last_name_cl','region_cl','adress_cl','phone_num_cl','facebook_cl']
        labels = {"first_name_cl'" : "","last_name_cl'" : "","region_cl'" : "","adress_cl'" : "","phone_num_cl'" : "","facebook_cl'" : ""}
