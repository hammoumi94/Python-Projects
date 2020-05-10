import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
import json
def index(request):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context)

