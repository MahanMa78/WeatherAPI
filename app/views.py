import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


load_dotenv()
# Create your views here.
def index(request):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={{}}&units=imperial&appid={api_key}'
    cities = City.objects.all() 
    
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    
    form = CityForm()
    
    weather_data = []
    
    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data , 'form' : form}
    
    return render(request, 'app/index.html' , context)