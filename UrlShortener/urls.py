from django.urls import include, path

from shortener.urls import urlpatterns as shortener_urls

urlpatterns = [
    path("", include(shortener_urls)),
]
