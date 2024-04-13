from django.shortcuts import render, redirect
from .models import Profile
from django.http import Http404
from .forms import ProfileForm
from django.urls import reverse


def profile_update_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(reverse('login'), next=reverse('profile_update'))

    user_ = request.user
    profile_ = user_.profile
    initial_ = {
        'first_name': user_.first_name,
        'last_name': user_.last_name,
        'email': user_.email,
        'bio': profile_.bio,
        'location': profile_.location
    }
    form = ProfileForm(data=request.POST or None,
                       instance=profile_, initial=initial_)
    if form.is_valid():
        form_obj = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user_.first_name = first_name
        user_.last_name = last_name
        user_.email = email
        user_.save()
        form_obj.save()
    context = {
        'form': form,
        'btn_label': 'Update Profile',
        'title': 'Update Profile'
    }
    return render(request, 'profiles/update.html', context=context)


def profile_detail_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    is_following = False
    if qs.exists():
        if request.user.is_authenticated:
            is_following = Profile.followers.contains(
                request.user)  # don't user in it's not efficient way
        context = {
            'username': qs.first(),
            'is_following': is_following
        }
        return render(request, template_name="profiles/details.html", context=context)
    raise Http404
