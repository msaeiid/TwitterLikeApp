from django.shortcuts import render
from .models import Profile
from django.http import Http404

def profile_detail_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    if qs.exists():
        context = {'username': qs.first()}
        return render(request, template_name="profiles/details.html", context=context)
    raise Http404
