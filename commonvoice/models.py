from django.db import models


def upload_to(instance, filename):
    return f'recordings/{instance.common_voice_id}.webm'


class Recording(models.Model):
    common_voice_id = models.CharField(max_length=100, default="-")
    text = models.TextField()
    recording = models.FileField(upload_to=upload_to, blank=False, null=False)
    correct_count = models.IntegerField(default=0)
    incorrect_count = models.IntegerField(default=0)
