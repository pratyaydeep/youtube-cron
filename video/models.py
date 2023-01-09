from django.db import models

# Create your models here.
class Video(models.Model):
  title = models.TextField()
  video_id = models.TextField()
  publish_time = models.TextField()
  description = models.TextField()
  thumbnail = models.TextField()
  
  class Meta:
    constraints=[
      models.UniqueConstraint(fields=['video_id'],name="unique_videoId_youtube")
    ]
    ordering = ('-publish_time',)
  
  def __str__(self):
    return self.title