from django.db import models
import random
from django.conf import settings

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tweet')

    def __str__(self) -> str:
        return f'{self.pk}'
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def serialize(self):
        return {
            'id': self.pk,
            'content': self.content,
            'likes': random.randint(1, 2024)
        }
