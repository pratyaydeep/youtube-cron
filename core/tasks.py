from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os



logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")

@shared_task
def search_youtube():
  from video.models import Video
  api_key = os.environ.get('API_KEY')
  link = 'https://youtube.googleapis.com/youtube/v3/search'
  published_after = datetime.now() - relativedelta(minutes=10)
  params = {
    'part' : 'snippet',
    'maxResults' : '2',
    'q' : 'cricket',
    'key' : api_key,
    'publishedAfter' : published_after.strftime('%Y-%m-%dT%H:%M:%SZ'),
    'type' : 'video',
    'order' : 'date'
  }
  response = requests.get(link, params)
  logger.info(response.json())
  if response.status_code==400:
    logger.info('API Key Expired')
  elif response.status_code==200:
    items = response.json().get('items',[])
    for item in items:
      video_id = item['id']['videoId']
      title = item['snippet']['title']
      publish_time = item['snippet']['publishTime']
      description = item['snippet']['description']
      thumbnail = item['snippet']['thumbnails']['default']['url']
      logger.info(title)
      video = Video(title=title,video_id=video_id,publish_time=publish_time,description=description,thumbnail=thumbnail)
      try:
        video.save()
        logger.info('Video Saved')
      except:
        logger.info('Entry Already Present')
  else:
    logger.info('Something Went Wrong during calling Youtube APIs')