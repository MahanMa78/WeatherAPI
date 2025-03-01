import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()
# Create your views here.
def index(request):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={{}}&units=imperial&appid={api_key}'
    city = 'Qazvin'
    city_weather = requests.get(url.format(city)).json()
    return render(request, 'app/index.html')