from django.db import models

# Create your models here.
# models.py
from django.db import models
# models.py
from django.db import models

from django.db import models

# class MyUser(models.Model):
#     username = models.CharField(max_length=100)  # Full name
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     address = models.TextField(blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     state = models.CharField(max_length=100, blank=True, null=True)
#     gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
#     profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)

#     def __str__(self):
#         return self.username

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, default='Unknown')  # or whatever default makes sense

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)

    caste = models.CharField(max_length=100, blank=True, null=True)  # ✅ Add this


    is_blocked = models.BooleanField(default=False)  # ✅ Add this field

    def __str__(self):
        return self.username


from django.db import models

class GirlsProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, default='Unknown')  # or whatever default makes sense 
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    def __str__(self):
        return self.name

class BoysProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, default='Unknown')  # or whatever default makes sense 
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    def __str__(self):
        return self.name

class DisabledProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, default='Unknown')  # or whatever default makes sense
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    def __str__(self):
        return self.name

class DivorcedProfile(models.Model):
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=100, default='Unknown')  # or whatever default makes sense
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='divorced_profiles/', default='profiles/default.png')

    def __str__(self):
        return self.name
