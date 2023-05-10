from django.urls import path

from . import views
from .views import redirect_short_url, create_short_url

urlpatterns = [
    path("", create_short_url, name="create_short_url"),
    path("<str:short_url>/", views.redirect_original, name="redirect_original"),
]
