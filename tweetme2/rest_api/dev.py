from rest_framework import authentication
from django.contrib.auth import get_user_model

User = get_user_model()


class DevAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        qs = User.objects.filter(id=4)
        user = qs.order_by("?").first()
        return (user, None)
