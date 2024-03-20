from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
import json


def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


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
