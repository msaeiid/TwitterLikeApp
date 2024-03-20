from django.shortcuts import HttpResponse, Http404
from .models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


def tweet_detail_view(request, pk, *args, **kwargs):
    try:
        tweet = Tweet.objects.get(id=pk)
    except:
        raise Http404
    return HttpResponse(f'<h1>Hello :{pk}</h1>')
