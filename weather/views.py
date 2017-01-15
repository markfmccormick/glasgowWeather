from django.shortcuts import render
from django.http import HttpResponse
from weather.get_weather import get_weather

# Create your views here.
def home(request):

    context_dict = get_weather()
    return render(request, 'weather/home.html', context_dict)
