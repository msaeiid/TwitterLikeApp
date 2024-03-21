from .models import Tweet
from django import forms

MAX_TWEET_LENGTH = 240


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content
