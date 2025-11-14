from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(DevelopersModel)
class DevelopersAdmin(admin.ModelAdmin):
    list_display=[
        "first_name",
        "last_name",
        "email",
        "age"
    ]

@admin.register(ProjectModel)
class ProjectsAdmin(admin.ModelAdmin):
    list_display=[
        "title"
    ]

@admin.register(SkillsModel)
class SkillsAdmin(admin.ModelAdmin):
    list_display=[
        "title"
    ]