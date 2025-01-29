import json

from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse

from shortener.models import Url


class TestShortener(TestCase):
    def setUp(self):
        self.client = Client()

    def test_shorten_url(self):
        response = self.client.post(
            "/",
            data=json.dumps(
                {"long_url": "https://www.example.com/this_is_a_long_url"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            response.data["short_url"].startswith("http://testserver/")
        )
        self.assertTrue(
            len(response.data["short_url"].split("/")[-2])
            == settings.SUFFIX_LENGTH
        )

    def test_shorten_url_bad_url_format(self):
        response = self.client.post(
            "/",
            data=json.dumps(
                {
                    "long_url": "www.example.com/this_is_a_long_url_incomplete_url"
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["long_url"], ["Enter a valid URL."])

    def test_shorten_url_wrong_method(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data["detail"].code, "method_not_allowed")

    def test_retrieve_long_url(self):
        long_url = "https://www.example.com/this_is_a_long_url"
        url = Url.objects.create(long_url=long_url)
        response = self.client.get(
            reverse("retrieve_long_url", args=[url.short_url])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["long_url"], long_url)

    def test_retrieve_long_url_wrong_short(self):
        long_url = "https://www.example.com/this_is_a_long_url"
        Url.objects.create(long_url=long_url)
        response = self.client.get(
            reverse("retrieve_long_url", args=["nonexistent_short_url"])
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"].code, "not_found")

    def test_retrieve_long_url_wrong_method(self):
        response = self.client.post(
            reverse("retrieve_long_url", args=["some_url"])
        )
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data["detail"].code, "method_not_allowed")
