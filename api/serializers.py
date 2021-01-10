from rest_framework import serializers 
from .models import *


class GetVenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'theme_night', 'people', 'current_music', 'average_age', 'sound_level')

class UpdateVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'people', 'average_age', 'sound_level')

