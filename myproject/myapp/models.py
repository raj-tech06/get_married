from django.db import models

# Create your models here.
# models.py
from django.db import models
# models.py
from django.db import models

from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, blank=True, null=True)  # ✅ keep only this one
    phone = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)  # ✅ Add this field
    birth_place = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    birth_time = models.TimeField(blank=True, null=True)  # ✅ Add this field
    about = models.TextField(blank=True, null=True)  # ✅ Add this field
    height = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    note = models.TextField(blank=True, null=True)  # ✅ Add this field
    education = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    occupation = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    father_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    mother_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field

    password = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)
    category = models.CharField(max_length=20, choices=[('girls', 'Girls'), ('boys', 'Boys'), ('disabled', 'Disabled'), ('divorced', 'Divorced')], null=True, blank=True)



    is_blocked = models.BooleanField(default=False)  # ✅ Add this field

    def __str__(self):
        return self.username




from django.db import models
from .models import MyUser  # ya jo bhi tumhara custom user model hai

class UserPhoto(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='user_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Photo"




from django.db import models

class GirlsProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, blank=True, null=True)  # ✅ keep only this one
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    dob = models.DateField(blank=True, null=True)  # ✅ Add this field
    birth_place = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    birth_time = models.TimeField(blank=True, null=True)  # ✅ Add this field
    about = models.TextField(blank=True, null=True)  # ✅ Add this field
    height = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    note = models.TextField(blank=True, null=True)  # ✅ Add this field
    education = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    occupation = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    father_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    mother_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    

    def __str__(self):
        return self.name

class GirlProfilePhoto(models.Model):
    girl = models.ForeignKey(GirlsProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='more_photos/')



class BoysProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, blank=True, null=True)  # ✅ keep only this one

    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    dob = models.DateField(blank=True, null=True)  # ✅ Add this field
    birth_place = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    birth_time = models.TimeField(blank=True, null=True)  # ✅ Add this field
    about = models.TextField(blank=True, null=True)  # ✅ Add this field
    height = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    note = models.TextField(blank=True, null=True)  # ✅ Add this field
    education = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    occupation = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    father_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    mother_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    

    def __str__(self):
        return self.name
    
class BoyProfilePhoto(models.Model):
    boy = models.ForeignKey(BoysProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='more_photos/')


class DisabledProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, blank=True, null=True)  # ✅ keep only this one
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    dob = models.DateField(blank=True, null=True)  # ✅ Add this field
    birth_place = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    birth_time = models.TimeField(blank=True, null=True)  # ✅ Add this field
    about = models.TextField(blank=True, null=True)  # ✅ Add this field
    height = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    note = models.TextField(blank=True, null=True)  # ✅ Add this field
    education = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    occupation = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    father_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    mother_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    

    def __str__(self):
        return self.name
    
class DisabledProfilePhoto(models.Model):
    disabled = models.ForeignKey(DisabledProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='more_photos/')    

class DivorcedProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, blank=True, null=True)  # ✅ keep only this one
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='divorced_profiles/', default='profiles/default.png')
    dob = models.DateField(blank=True, null=True)  # ✅ Add this field
    birth_place = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    birth_time = models.TimeField(blank=True, null=True)  # ✅ Add this field
    about = models.TextField(blank=True, null=True)  # ✅ Add this field
    height = models.CharField(max_length=10, blank=True, null=True)  # ✅ Add this field
    note = models.TextField(blank=True, null=True)  # ✅ Add this field
    education = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    occupation = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    father_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    mother_name = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this field
    

    def __str__(self):
        return self.name
        
class DivorcedProfilePhoto(models.Model):
    divorced = models.ForeignKey(DivorcedProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='more_photos/')



class ProfilePermission(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[
        ('boys', 'Boys'),
        ('girls', 'Girls'),
        ('disabled', 'Disabled'),
        ('divorced', 'Divorced')
    ])
    profile_email = models.EmailField()  # Email of the profile (like a girl/boy/etc)
