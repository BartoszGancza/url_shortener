from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer

from shortener.models import Url


class UrlCreateSerializer(ModelSerializer):
    short_url = serializers.SerializerMethodField(
        method_name="get_full_short_url"
    )

    class Meta:
        model = Url
        fields = ("short_url", "long_url")
        read_only_fields = ("short_url",)

    def get_full_short_url(self, obj):
        return reverse(
            "retrieve_long_url",
            args=[obj.short_url],
            request=self.context.get("request"),
        )


class UrlRetrieveSerializer(UrlCreateSerializer):
    class Meta:
        model = Url
        fields = ("long_url",)
