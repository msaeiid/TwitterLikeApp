from rest_framework import serializers
from .models import Tweet
from django.conf import settings
from profiles.serializers import ProfileSerializer
MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class TweetCreateSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes', 'author']

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value

    def get_likes(self, obj):
        return obj.likes.count()


class TweetSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)
    """if in some cases like below I want serializer field be different from model field -> og_tweet -> source='parent' is user like below
        og_tweet = TweetCreateSerializer(source='parent', read_only=True)
    """

    class Meta:
        model = Tweet
        fields = ['author', 'id', 'content', 'likes', 'is_retweet', 'parent']

    def get_likes(self, obj):
        return obj.likes.count()


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(required=False, allow_blank=True)

    def validate_action(self, value: str):
        value = value.lower()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError('Undefined action')
        return value
