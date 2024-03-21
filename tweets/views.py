from django.http import JsonResponse
from django.shortcuts import render
from .models import Tweet
import random
from .forms import TweetForm
from django.shortcuts import redirect
from django.urls import reverse

def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(data=request.POST or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.save()
        form = TweetForm()
        return redirect(reverse('tweets:home'))
    return render(request, template_name='components/forms.html', context={"form": form})



def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweets_lst = [{"id": tweet.id, "content": tweet.content, "likes": random.randint(1, 2023)}
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
