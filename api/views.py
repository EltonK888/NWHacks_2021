from django.shortcuts import render
from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import * 


@api_view(['GET'])
def api_overview(request):
    api = {
        'Returns List of All Venue Objects': 'get_venues/', 
        'Updates # of People and Average Age of Venue using Venue ID and User Age': 'update_venue/<int:pk>/',
    }

    return Response(api)

class VenuesList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = GetVenuesSerializer

def calculate_new_average_age(age, venue_id): 
    venue = Venue.objects.get(id=pk)
    total_age = venue.average_age * venue.people
    total_age += age
    new_average_age = total_age / (venue.people + 1)
    return new_average_age


@api_view(['POST'])
def add_new_person(request, pk): 
    venue = Venue.objects.get(id=pk)
    new_age = request.data["age"]
    new_average_age = calculate_new_average_age(new_age)
    new_people = venue.people + 1

    data = {
        "people": new_people, 
        "average_age": new_average_age
    }

    serializer = UpdateVenueSerializer(instance=venue, data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(data={
            "failure": "Updating venue failed"
        })




