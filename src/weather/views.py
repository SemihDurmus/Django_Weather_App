from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
import requests
from pprint import pprint
from .models import City
from .forms import CityForm
from django.contrib import messages


def index(request):
    url = config("BASE_URL")

    form = CityForm
    cities = City.objects.all()
    city_data = []

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["name"]  # request.POST.get("name")
            if not City.objects.filter(name=new_city).exists():
                r = requests.get(url.format(new_city))
                if r.status_code == 200:
                    form.save()
                    messages.success(request, "City added successfully")
                else:
                    messages.warning(request, "City not found")
            else:
                messages.warning(request, "City already exist")
            return redirect("home")
    for city in cities:
        r = requests.get(url.format(city))
        content = r.json()

        weather_data = {
            "city": city.name,
            "temp": content["main"]["temp"],
            "description": content["weather"][0]["description"],
            "icon": content["weather"][0]["icon"],
        }
        city_data.append(weather_data)
    # pprint(city_data)
    context = {
        "city_data": city_data,
        "form": form
    }
    return render(request, "weather/index.html", context)


def delete(request, city):
    item = City.objects.get(name=city)
    if request.method == "POST":
        item.delete()
        return redirect("home")
    context = {
        "item": item
    }
    return render(request, "weather/delete.html", context)
