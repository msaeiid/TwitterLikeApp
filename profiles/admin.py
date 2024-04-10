from django.contrib import admin
from .models import Profile, FollowRelation


@admin.register(FollowRelation)
class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'profile', 'timestamp']


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'timestamp']
