from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class FollowRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(
        User, through=FollowRelation, related_name='following', blank=True)
    """project_obj = Profile.objects.first()
       project_obj.followers.all() -> All users following this profile
       user.following.all() -> All profiles I follow
    """



    def __str__(self) -> str:
        return self.user.username
