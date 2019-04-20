from django.urls import path

from commonvoice.views import RecordingsView, RecordingView, pick_random_recording

urlpatterns = [
    path('recordings', RecordingsView.as_view()),
    path('recordings/imfeelinglucky', pick_random_recording),
    path('recordings/<int:pk>', RecordingView.as_view(), name="recording"),
]
