from django.urls import path

from commonvoice.views import RecordingsView

urlpatterns = [
    path('recordings', RecordingsView.as_view())
]
