from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})


def feed_view(request, *args, **kwargs):
    return render(request, template_name='pages/feed.html')


def tweet_list_view(request, *args, **kwargs):
    return render(request, template_name="tweets/list.html")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    context = {'tweetId': tweet_id}
    return render(request, template_name="tweets/detail.html", context=context)
