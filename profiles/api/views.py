from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (api_view,
                                       permission_classes)
from rest_framework import permissions
from django.contrib.auth import get_user_model


User = get_user_model()


@api_view(http_method_names=(['POST', 'GET']))
@permission_classes([permissions.IsAuthenticated])
def user_follow_view(request, username, *args, **kwargs):
    current_user = request.user
    followed_user = User.objects.filter(username=username)

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
