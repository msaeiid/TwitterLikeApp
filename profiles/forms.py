from django.contrib.auth import get_user_model
from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['first_name',  'last_name', 'email', 'location', 'bio']
