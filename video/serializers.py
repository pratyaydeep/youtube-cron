from rest_framework import serializers
from . import models


class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'video_id',
      'title',
      'description',
      'publish_time',
      'thumbnail'
    )
    model = models.Video