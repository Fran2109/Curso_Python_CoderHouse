from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank = True)
    link = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.avatar}"