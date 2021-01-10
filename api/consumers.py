from channels.generic.websockets import AsyncWebsocketConsumer
import json

from .models import *


class VenuesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_group_name = 'realtime-venue-data'

        await self.channel_layer.group_add(
            self.channel_group_name, 
            self.channel_name
        )

        await self.accept()

    async def recieve(self, text_data):
        pass

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.channel_group_name, 
            self.channel_name
        )

    async def send_venues(self, event):
        print(event)
        venues = event["venues"]
        print("Sending Venues to Websocket")
        await self.send(text_data=json.dumps({
            'venues': venues
        }))

