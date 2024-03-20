from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet
import json


def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})


def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweets_lst = [{"id": tweet.id, "content": tweet.content}
                  for tweet in tweets]
    data = {
        'isUser': False,
        'response': tweets_lst
    }
    return JsonResponse(data)


def tweet_detail_view(request, pk, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift/Java/iOS/Android
    return json data
    """
    data = {}
    status = 200
    try:
        tweet = Tweet.objects.get(id=pk)
        data['content'] = tweet.content
    except:
        status = 404
        data["message"] = "Not Found"
    return JsonResponse(data=data, status=status)
