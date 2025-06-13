from django.db import models

# Create your models here.
# models.py
from django.db import models
# models.py
from django.db import models

from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100)  # Full name
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)

    def __str__(self):
        return self.username


