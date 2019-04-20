import random

from django.http import HttpResponseRedirect

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from commonvoice.models import Recording
from commonvoice.serializers import RecordingsSerializer, RecordingSerializer


class RecordingsView(ListCreateAPIView):
    queryset = Recording.objects.all()
    serializer_class = RecordingsSerializer


class RecordingView(RetrieveAPIView):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

    def post(self, request, pk):
        recording = Recording.objects.get(id=pk)
        recording.correct_count += 1
        recording.save()
        return Response({
            "message": "Marked as correct",
            "id": pk
        })

    def delete(self, request, pk):
        recording = Recording.objects.get(id=pk)
        recording.incorrect_count += 1
        recording.save()
        return Response({
            "message": "Marked as incorrect",
            "id": pk
        })


def pick_random_recording(request):
    if request.method == 'GET':
        pk = random.randrange(1, Recording.objects.all().count() + 1)
        return HttpResponseRedirect(
            reverse(
                viewname="recording",
                kwargs={'pk': pk},
                request=request
            )
        )
