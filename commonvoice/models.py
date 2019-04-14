from django.db import models


def upload_to(instance, filename):
    return f'recordings/{instance.id}.webm'


class Recording(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    text = models.TextField()
    recording = models.FileField(upload_to=upload_to, blank=False, null=False)
