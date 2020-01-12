from django.shortcuts import render
import requests
from .models import weatherModel
from .forms import CityForm
# Create your views here.
def weather_view(request,*args,**kwargs):
    if request.method == "POST":
        pass
    myform = CityForm()

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=716806f2f07ef0d6d7a6bcec3c866551"
    weather_data = []
    cities = weatherModel.objects.all()
    for city in cities:
        result = requests.get(url.format(city)).json()
        city_weather = {
            "city":city.name,
            # "description":result['weather'][0]['description'],
            # "temparature":result['main']['temp'],
            # "icon":result['weather'][0]['icon']
        }
        weather_data.append(city_weather)
        
    context = { 
        "weather_data":weather_data
    }
    return render(request,'weather_update.html',context)