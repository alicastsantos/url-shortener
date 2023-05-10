from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from .forms import URLShortenerForm
from .models import URL


def index(request):
    return render(request, "shortener/index.html", {})


def redirect_short_url(request, short_id):
    short_url = get_object_or_404(URL, short_id=short_id)

    short_url.access_count += 1
    short_url.save()

    return HttpResponseRedirect(short_url.original_url)


def create_short_url(request):
    if request.method == "POST":
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            original_url = form.data["original_url"]
            print(original_url)
            shortened_url = URL.objects.create(original_url=original_url)
            shortened_url.save()
            redirect_url = reverse(
                "redirect_original", kwargs={"short_url": shortened_url.short_url}
            )
            return render(
                request,
                "shortener/index.html",
                {"shortened_url": shortened_url, "redirect_url": redirect_url},
            )
    else:
        form = URLShortenerForm()
    return render(request, "shortener/index.html", {"form": form})


def redirect_original(request, shortened_url):
    url = get_object_or_404(URL, short_url=shortened_url)
    url.visits += 1
    url.save()
    return redirect(url.original_url)
