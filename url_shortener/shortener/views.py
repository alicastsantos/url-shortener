from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import URLShortenerForm
from .models import URL


def index(request):
    return render(request, "shortener/index.html", {})


def handle_post(request):
    if request.method == "POST":
        form = URLShortenerForm(request.POST)

        if form.is_valid():
            original_url = form.data["original_url"]
            shortened_url = generate_short_url(original_url)

            return render(
                request,
                "shortener/index.html",
                {
                    "shortened_url": shortened_url,
                    "original_url": original_url,
                    "form": form,
                },
            )
    else:
        form = URLShortenerForm()
    return render(request, "shortener/index.html", {"form": form})


def generate_short_url(original_url):
    url_obj = URL.objects.filter(original_url=original_url).first()

    if not url_obj:
        url_obj = URL.objects.create(original_url=original_url)

    return url_obj.short_url


def redirect_to_original_url(_, shortened_url):
    original_url = URL.objects.filter(short_url=shortened_url).first().original_url
    url = get_object_or_404(URL, original_url=original_url)
    url.update_last_access()
    return HttpResponseRedirect("https://" + url.original_url)
