from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (api_view,
                                       permission_classes)
from rest_framework import permissions
from django.contrib.auth import get_user_model
from ..serializers import ProfileSerializer
from ..models import Profile


User = get_user_model()


@api_view(http_method_names=(['POST', 'GET']))
@permission_classes([permissions.IsAuthenticated])
def user_follow_view(request, username, *args, **kwargs):
    current_user = request.user
    followed_user = User.objects.filter(username=username)

    # prevent user fom following itself, Its not a good practice to do it here we can handle it with a signal on save or create of FollowRelation to check user and profile are not same...
    if current_user == followed_user.first():
        data = {
            'count': current_user.profile.followers.count()
        }
        return Response(data=data, status=status.HTTP_200_OK)

    if not followed_user.exists():
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    followed_user = followed_user.first()
    data = {}
    action = request.data.get('action') or None
    if action == 'follow':
        followed_user.profile.followers.add(current_user)
    elif action == 'unfollow':
        followed_user.profile.followers.remove(current_user)
    else:
        pass
    data = {
        'count': followed_user.profile.followers.count()
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(http_method_names=(['GET']))
def profile_detail_api_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
    profile = qs.first()
    serializer = ProfileSerializer(instance=profile)
    return Response(serializer.data, status=status.HTTP_200_OK)
