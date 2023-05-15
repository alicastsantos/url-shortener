from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from urllib.parse import urljoin
from .models import URL


def validate_url(original_url):
    url_validator = URLValidator()

    if not original_url.startswith(("http://", "https://")):
        original_url = urljoin("https://", original_url)

    try:
        url_validator(original_url)
    except ValidationError as e:
        raise forms.ValidationError("Please enter a valid URL")


class URLShortenerForm(forms.Form):
    original_url = forms.CharField(
        label="URL to Shroten",
        max_length=2048,
        validators=[validate_url],
        error_messages={"invalid": "Please enter a valid URL"},
    )

    class Meta:
        model = URL
        fields = ["original_url"]
