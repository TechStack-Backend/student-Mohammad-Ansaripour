from django.contrib import admin
from .models import *

# Register your models here.
class SkillsInLine(admin.TabularInline):
    model = SkillModel.developers.through
    extra=1

@admin.register(DevelopersModel)
class DevelopersAdmin(admin.ModelAdmin):

    list_display=[
        "username",
        "first_name",
        "last_name",
    ]
    inlines=[SkillsInLine]
    def skills_list(self,obj):
        pass




@admin.register(SkillModel)
class SkillAdmins(admin.ModelAdmin):
    list_display=[
        "skill"
    ]