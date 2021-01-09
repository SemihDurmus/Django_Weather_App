from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from .models import City


def index(request):
    url = config("BASE_URL")

    cities = City.objects.all()
    city_data = []

    for city in cities:
        r = requests.get(url.format(city))
        returned_data = r.json()

        weather_data = {
            "city": city.name,
            "temp": returned_data["main"]["temp"],
            "description": returned_data["weather"][0]["description"],
            "icon": returned_data["weather"][0]["icon"],
        }
        city_data.append(weather_data)
    pprint(city_data)
    context = {
        "city_data": city_data
    }
    return render(request, "weather/index.html", context)
