from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint


def index(request):
    url = config("BASE_URL")
    city = "Berlin"
    r = requests.get(url.format(city))
    returned_data = r.json()
    # print(type(returned_data))
    # pprint(returned_data)
    context = {
        "city": city,
        "temp": returned_data["main"]["temp"],
        "description": returned_data["weather"][0]["description"],
        "icon": returned_data["weather"][0]["icon"],
    }
    return render(request, "weather/index.html", context)
