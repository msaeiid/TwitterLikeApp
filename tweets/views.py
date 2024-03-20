from django.shortcuts import render
from django.shortcuts import HttpResponse


def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


def tweet_detail_view(request, pk, *args, **kwargs):
    return HttpResponse(f'<h1>Hello :{pk}</h1>')
