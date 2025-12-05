from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display=[
        "bio",
        "user",
    ]
