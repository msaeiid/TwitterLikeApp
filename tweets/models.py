from django.db import models


class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    # in tutorial he used FileField
    image = models.ImageField(upload_to='tweets/', blank=True, null=True)
