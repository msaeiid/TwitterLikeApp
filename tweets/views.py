from django.http import JsonResponse
from django.shortcuts import render
from .models import Tweet
import random
from .forms import TweetForm
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})


def tweet_create_view(request, *args, **kwargs):
    """
    REST API create Views -> DRF
    """
    if not request.user.is_authenticated:
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)

    form = TweetForm(data=request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user  # or None  ## if user null=True in tweet model
        tweet.save()
        # to check if request is ajax or not
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            return JsonResponse(tweet.serialize(), status=201)
        form = TweetForm()
        if next_url and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        return JsonResponse(form.errors, status=400)
    return render(request, template_name='components/forms.html', context={"form": form})



def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweets_lst = [tweet.serialize() for tweet in tweets]
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
