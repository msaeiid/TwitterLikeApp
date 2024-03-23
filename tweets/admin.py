from django.contrib import admin
from .models import Tweet


class CustomTweet(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['user__username', 'user__email']


admin.site.register(Tweet, CustomTweet)
