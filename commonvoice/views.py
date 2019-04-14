from rest_framework.generics import ListCreateAPIView

from commonvoice.models import Recording
from commonvoice.serializers import RecordingSerializer


class RecordingsView(ListCreateAPIView):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
