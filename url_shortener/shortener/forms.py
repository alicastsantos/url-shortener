from django import forms
from .models import URL


class URLShortenerForm(forms.ModelForm):
    original_url = forms.URLField(
        label="Original URL",
        max_length=2048,
        error_messages={"invalid": "Please enter a valid URL"},
    )

    class Meta:
        model = URL
        fields = ["original_url"]
