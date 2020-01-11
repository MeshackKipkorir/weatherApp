from django.shortcuts import render
import requests
# Create your views here.
def weather_view(request,*args,**kwargs):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=716806f2f07ef0d6d7a6bcec3c866551"
    city = "Nairobi"
    result = requests.get(url.format(city)).json()
    print(result['main']['temp'] - result['weather'][0])
    city_weather = {
        "city":city,
        "icon":result['weather'][0]['icon'],
        "temparature":result['main']['temp'],
        "description":result['weather'][0]['description']
    }
    return render(request,'weather_update.html',city_weather)