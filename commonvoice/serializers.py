from rest_framework import serializers

from commonvoice.models import Recording


class RecordingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = ("common_voice_id", "text", "recording", "id")


class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = "__all__"
