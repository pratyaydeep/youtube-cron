from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer
from django.db.models import Q

# class ListVideo(generics.ListCreateAPIView):
#     queryset = models.Video.objects.all()
#     serializer_class = VideoSerializer

# longitude = self.request.query_params.get('longitude')

@api_view(['GET'])
def search_video(self):
  search_string = self.query_params.get('s')
  if search_string:
    videos = Video.objects.filter(Q(title__icontains=search_string) | Q(description__icontains=search_string)).all()
    serializer=VideoSerializer(videos,many=True)
    return Response(serializer.data)
  else:
    videos = Video.objects.all()
    serializer=VideoSerializer(videos,many=True)
    return Response(serializer.data)
  