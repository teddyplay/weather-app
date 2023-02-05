import requests
from django.shortcuts import render


def index(reqest):
    appid = 'f809d633cb3382370d3617182698fd3e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'London'
    response = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': response["main"]["temp"],
        'icon': response["weather"][0]["icon"]
    }

    context = {
        'info': city_info
    }
    return render(reqest, 'weatherfront/index.html', context)
