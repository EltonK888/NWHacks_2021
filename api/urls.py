from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="API Overview"), 
    path('get_venues/', views.VenuesList.as_view(), name="Get Venues"), 
    path('update_venue/<int:pk>/', views.add_new_person, name="Send New Person"), 
]