from django.shortcuts import render
import requests
from .models import State

def home(request):
    # Fetch data from the API
    response = requests.get('https://apistate.pythonanywhere.com/')
    data = response.json()

    # Save data to the database
    for item in data:
        state = State(name=item['name'], capital=item['capital'])
        state.save()

    # Get all countries from the database
    states = State.objects.all()

    return render(request, 'home.html', {'state': states})

