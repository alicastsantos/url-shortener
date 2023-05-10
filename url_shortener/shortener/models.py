import string
import random
from django.db import models
from django.urls import reverse


def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(length))


class URL(models.Model):
    original_url = models.URLField(max_length=2048, primary_key=True)
    short_url = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.original_url

    def generate_short_url(self):
        return generate_random_string(length=8)

    def get_short_url(self):
        return f"http://localhost:8000/{self.short_url}/"

    def get_absolute_url(self):
        return reverse("url_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.short_url:
            while True:
                short_url = self.generate_short_url()
                if not URL.objects.filter(short_url=short_url).exists():
                    self.short_url = short_url
                    break
        super().save(*args, **kwargs)
