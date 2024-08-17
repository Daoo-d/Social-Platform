from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatar/",null=True,blank=True)
    fullname = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    location = models.CharField(max_length=30,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)