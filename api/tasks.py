from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep 
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import * 
from .serializers import * 

from random import randint, uniform


# Update venue data periodically 
# 1. Updates venue data
# 2. Runs venue through machine learning model 
# 3. Updates venue with new fun factor 

@shared_task
def update_venues(): 
    print("Updating venue data")
    venues = Venue.objects.all()
    
    for venue in venues:
        new_people = randint(-3, 3)
        new_age = round(uniform(-3, 3))
        venue.people = venue.people + new_people
        total_age = venue.average_age * venue.people
        total_age += new_age
        new_average_age = total_age / (venue.people + 1)
        venue.average_age = new_average_age
        sound_level_change = randint(-3, 3)
        venue.sound_level += sound_level_change
        venue.save()

@shared_task(name="get-venues-task")
def get_venues():
    print("Getting venues")
    venues = Venue.objects.all()
    serializer = GetVenuesSerializer(venues, many=True)
    channel_layer = get_channel_layer()
    message = {
        "type": "send_venues", 
        "venues": serializer.data
    }
    async_to_sync(channel_layer.group_send)('realtime-venue-data', message)

while True:
    sleep(5)
    update_venues()
    get_venues()