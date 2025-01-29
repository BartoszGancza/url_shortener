from rest_framework.generics import CreateAPIView, RetrieveAPIView

from shortener.models import Url
from shortener.serializers import UrlCreateSerializer, UrlRetrieveSerializer


# There is a couple different ways to realize this functionality, like using pure APIView
# with custom implemented post and get methods, using pure Django views, using mixins, but this one
# is (in my mind) the cleanest and leverages mechanisms provided by DRF without having to write
# a lot of custom code.
class UrlShortenView(CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlCreateSerializer
    authentication_classes = []
    permission_classes = []


class RetrieveLongUrlView(RetrieveAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlRetrieveSerializer
    authentication_classes = []
    permission_classes = []
    lookup_field = "short_url"

    # If we wanted to instantly redirect the users to a proper URL instead of just returning
    # the value, we can just override get method.

    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     return redirect(instance.long_url)
