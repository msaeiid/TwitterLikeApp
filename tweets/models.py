from django.db import models
import random

class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    # in tutorial he used FileField
    image = models.ImageField(upload_to='tweets/', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id}'

    def serialize(self):
        return {
            'id': self.pk,
            'content': self.content,
            'likes': random.randint(1, 2024)
        }
