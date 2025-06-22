from django import forms
from .models import UserPhoto  # ye model tumne pehle banaya hoga

class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['image']
