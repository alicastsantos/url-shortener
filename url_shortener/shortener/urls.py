from django.urls import path

from . import views
from .views import handle_post

urlpatterns = [
    path("", handle_post, name="handle_post"),
    path(
        "<str:shortened_url>/",
        views.redirect_to_original_url,
        name="redirect_to_original_url",
    ),
]
