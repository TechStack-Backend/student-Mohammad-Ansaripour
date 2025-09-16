from django.db import models
from django.urls import reverse


class DevelopersModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=75)
    email=models.EmailField()
    username=models.CharField(max_length=50,blank=True,unique=True)
    age=models.PositiveIntegerField()
    projects=models.ManyToManyField("ProjectModel",related_name="developers")

    class Meta:
        ordering=['last_name']
    def get_absolute_url(self):
        return reverse("developers:developers_detail", kwargs={"username" : self.username})

    def __str__(self):
        return self.first_name + self.last_name
    
class SkillsModel(models.Model):
    title=models.CharField(max_length=30)
    desciption=models.TextField()
    developer=models.ForeignKey("DevelopersModel",on_delete=models.CASCADE,related_name="skills",)

    def __str__(self):
        return self.title

class ProjectModel(models.Model):
    title=models.CharField(max_length=30)
    desciption=models.TextField()

    def get_absolute_url(self):
        return reverse("developers:projects_detail", kwargs={"id" : self.id})

    def __str__(self):
        return self.title
