from django.db import models
from django.urls import reverse


# Create your models here.
class SkillModel(models.Model):

    skill=models.CharField(max_length=50)
    skills=models.ForeignKey('DevelopersModel',on_delete=models.DO_NOTHING,related_name="skills")

class DevelopersModel(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    
    def get_obsolute_url(self):
        return reverse("DevInfoApp:developerDetail",kwargs={"username": self.username })