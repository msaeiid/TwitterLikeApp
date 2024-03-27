from django.http import JsonResponse
from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from rest_framework import status
from .serializers import (TweetSerializer,
                          TweetActionSerializer,
                          TweetCreateSerializer)
from rest_framework.response import Response
from rest_framework.decorators import (api_view,
                                       permission_classes,
                                       authentication_classes)
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})

# pure django

def tweet_create_view_pure_django(request, *args, **kwargs):
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


def tweet_list_view_pure_django(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweets_lst = [tweet.serialize() for tweet in tweets]
    data = {
        'isUser': False,
        'response': tweets_lst
    }
    return JsonResponse(data)


def tweet_detail_view_pure_django(request, pk, *args, **kwargs):
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

# django rest framework- method based views


@api_view(http_method_names=['POST'])
@permission_classes([permissions.IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET'])
def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    serializers = TweetSerializer(instance=tweets, many=True)
    return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def tweet_detail_view(request, pk, *args, **kwargs):
    tweet = Tweet.objects.filter(id=pk)
    if not tweet.exists():
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serialize = TweetSerializer(tweet.first())
        return Response(data=serialize.data, status=status.HTTP_200_OK)


@api_view(http_method_names=(['DELETE', 'POST']))
@permission_classes([permissions.IsAuthenticated])
def tweet_delete_view(request, pk, *args, **kwargs):
    tweets = Tweet.objects.filter(pk=pk)
    if not tweets.exists():
        return Response({"message": "Requested tweet not found!"}, status=status.HTTP_404_NOT_FOUND)
    tweets = tweets.filter(user=request.user)
    if not tweets.exists():
        return Response({"message": "You can't delete this tweet"}, status=status.HTTP_401_UNAUTHORIZED)
    tweets.first().delete()
    return Response({"message": "Tweet has been deleted!"}, status=status.HTTP_204_NO_CONTENT)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def tweet_action_view(request,  *args, **kwargs):
    """
    id is required.
    Action options are:like,unlike,retweet
    """
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        tweet_id = serializer.validated_data.get('id')
        action = serializer.validated_data.get('action')
        content = serializer.validated_data.get('content') or None

        tweet = Tweet.objects.filter(pk=tweet_id)
        if not tweet.exists():
            return Response({"Message": "Tweet Not Found"}, status=status.HTTP_404_NOT_FOUND)

        tweet = tweet.first()

        if action == "like":
            # if not tweet.likes.filter(user=request.user).exists():
            tweet.likes.add(request.user)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif action == "unlike":
            # if tweet.likes.filter(user=request.user).exists():
            tweet.likes.remove(request.user)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif action == "retweet":
            new_tweet = Tweet.objects.create(user=request.user,
                                             parent=tweet,
                                             content=content)
            # I should return the retweet obj so
            serializer = TweetSerializer(new_tweet)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
