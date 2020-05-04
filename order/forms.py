from django import forms
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bookorder,Order,Orderdetail

class OrdercheckoutForm(forms.ModelForm):
    class Meta:
      model = Orderdetail
      fields = ['first_name','last_name','region_adress','town_adress','city_adress','street_adress','postal_code','phone_num','email','shipping_type','paying_type']
