# my_app/views.py
# my_app/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Event, Athlete, Medal

def olympic_events(request):
    # Fetch the list of Olympic events from the database
    events = Event.objects.all()

    # Pass the list of events to the template
    return render(request, 'olympic_events.html', {'events': events})

def athlete_list(request):
    # Fetch the list of athletes from the database
    athletes = Athlete.objects.all()

    # Pass the list of athletes to the template
    return render(request, 'athlete_list.html', {'athletes': athletes})

def athlete_details(request, athlete_id):
    # Fetch the specific athlete from the database
    athlete = get_object_or_404(Athlete, id=athlete_id)

    # Pass the athlete data to the template
    return render(request, 'athlete_details.html', {'athlete': athlete})

def medal_tally(request):
    # Calculate medal tally for each country
    medal_tally = Medal.objects.values('country').annotate(
        gold_count=Count('medal', filter=Medal.medal_type == 'Gold'),
        silver_count=Count('medal', filter=Medal.medal_type == 'Silver'),
        bronze_count=Count('medal', filter=Medal.medal_type == 'Bronze')
    )

    # Pass the medal tally data to the template
    return render(request, 'medal_tally.html', {'medal_tally': medal_tally})

def event_details(request, event_id):
    # Fetch the specific event from the database
    event = get_object_or_404(Event, id=event_id)

    # Pass the event data to the template
    return render(request, 'event_details.html', {'event': event})

    