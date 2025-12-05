from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(null=True)
    img=models.ImageField(upload_to="profile/",null=True)
    
    def __str__(self):
        return self.user.get_full_name()
