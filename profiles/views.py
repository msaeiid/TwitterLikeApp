from django.shortcuts import render

from django.conf import settings

User = settings.AUTH_USER_MODEL


def profile_detail_view(request, username, *args, **kwargs):
    context = {'username': username}
    return render(request, template_name="profiles/details.html", context=context)
