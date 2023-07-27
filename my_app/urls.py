from django.urls import path
from . import views  # Import the views module from the same app

urlpatterns = [
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    path('athletes/', views.athlete_list, name='athlete_list'),
    path('athlete/<int:athlete_id>/', views.athlete_details, name='athlete_details'),
    path('medal-tally/', views.medal_tally, name='medal_tally'),
]
