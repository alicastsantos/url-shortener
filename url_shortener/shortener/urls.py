from django.urls import path

from . import views
from .views import create_short_url

urlpatterns = [
    path("", create_short_url, name="create_short_url"),
    path("<str:shortened_url>/", views.redirect_original, name="redirect_original"),
]
