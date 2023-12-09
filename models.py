from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to='userthings/')

    def __str__(self):
        return self.user_profile