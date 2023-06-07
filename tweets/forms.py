from typing import Any, Dict
from django import forms
from tweets.models import Tweet
content_size = 250

class Tweetform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(self) > content_size:
            raise forms.ValidationError(" Tweet size can not exceed " + content_size + " characters.");
        return content