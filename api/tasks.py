from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep 
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import * 
from .serializers import * 

from random import randint, uniform

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
import math


# Update venue data periodically 
# 1. Updates venue data
# 2. Runs venue through machine learning model 
# 3. Updates venue with new fun factor 

@shared_task
def update_venues(): 
    print("Updating venue data")
    venues = Venue.objects.all()

    # data = pd.read_csv('api/regression-data.csv')

    # training_data = data[data["type"] == "training"]

    # X_train = training_data[[ 'numberPeople', 'hasTheme', 'soundLevel', 'averageAge' ]]
    # Y_train = training_data['funFactor']

    # regr = LinearRegression()
    # regr.fit(X_train, Y_train)

    # X2_train = sm.add_constant(X_train)
    # est = sm.OLS(Y_train, X2_train)
    # est2 = est.fit()
    
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
        # venue_ML = pd.DataFrame(venue, columns=['people', 'theme_night', 'sound_level', 'average_age'], index=['people','theme_night', 'sound_level', 'average_age'])
        # fun_factor = regr.predict(venue_ML)
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