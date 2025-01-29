from django.urls import path

from shortener.views import RetrieveLongUrlView, UrlShortenView

urlpatterns = [
    path(
        "",
        UrlShortenView.as_view(),
        name="shorten_url",
    ),
    path(
        "<str:short_url>/",
        RetrieveLongUrlView.as_view(),
        name="retrieve_long_url",
    ),
]
