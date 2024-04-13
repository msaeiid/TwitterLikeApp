from django.db import models
import random
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tweet')

    def __str__(self) -> str:
        return f'{self.pk}'


class TweetQuerySet(models.QuerySet):
    # it query comes after all()
    def feed(self, user):
        profiles_exit = user.following.exists()
        follower_users_id = user.following.values_list(
            'user__id', flat=True)
        return self.filter(
            Q(user__id__in=follower_users_id) |
            Q(user=user)
        ).distinct('pk').order_by('-timestamp')


class TweetManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return TweetQuerySet(self.model, using=self._db)

    # it query comes after objects()
    def feed(self, user):
        return self.get_queryset().feed(user)


class Tweet(models.Model):
    # it is used for retweeting
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tweets')
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # in tutorial he used FileField
    image = models.ImageField(upload_to='tweets/', blank=True, null=True)

    class Meta():
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.id}'

    @property
    def is_retweet(self):
        return self.parent is not None

    objects = TweetManager()
