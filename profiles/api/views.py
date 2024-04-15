from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (api_view,
                                       permission_classes)
from rest_framework import permissions
from django.contrib.auth import get_user_model
from ..serializers import ProfileSerializer
from ..models import Profile


User = get_user_model()


@api_view(http_method_names=(['GET', 'POST']))
def profile_detail_api_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
    profile = qs.first()
    if request.method == "POST":
        current_user = request.user
        if current_user != profile.user:
            data = {}
            action = request.data.get('action') or None
            if action == 'follow':
                profile.followers.add(current_user)
            elif action == 'unfollow':
                profile.followers.remove(current_user)
            else:
                pass
    serializer = ProfileSerializer(
        instance=profile, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
