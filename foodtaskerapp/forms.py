from django import forms
from django.contrib.auth.models import User
from foodtaskerapp.models import Restaurant

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','phone','address','logo')
