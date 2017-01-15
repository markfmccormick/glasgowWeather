import pyowm

#Using my free API key
owm = pyowm.OWM('e9f9ea5a4a3f9fd742f10d1a0e2f4e12')

def get_weather():

    results = {'weather': {}, 'forecast': []}

    #Get currently observed weather in glasgow
    obs = owm.weather_at_id(2648579) #City ID for Glasgow, UK

    #Get weather object
    weather = obs.get_weather()

    #Get location info from weather object
    location = obs.get_location()

    results['weather']['location'] = location.get_name()
    results['weather']['time'] = weather.get_reference_time(timeformat='iso')
    results['weather']['description'] = weather.get_detailed_status()
    results['weather']['temperature'] = float("{0:.1f}".format(weather.get_temperature()['temp']-273.15))
    results['weather']['temp_max'] = float("{0:.1f}".format(weather.get_temperature()['temp_max']-273.15))
    results['weather']['temp_min'] = float("{0:.1f}".format(weather.get_temperature()['temp_min']-273.15))
    #results['weather']['wind_direction'] = weather.get_wind()['deg']
    results['weather']['wind_speed'] = weather.get_wind()['speed']
    results['weather']['clouds'] = weather.get_clouds()
    results['weather']['humidity'] = weather.get_humidity()
    results['weather']['pressure'] = weather.get_pressure()['press']
    results['weather']['sunrise_time'] = weather.get_sunrise_time('iso')
    results['weather']['sunset_time'] = weather.get_sunset_time('iso')

    #Get 3 hour forecast format
    forecast = owm.three_hours_forecast('Glasgow,uk')
    f = forecast.get_forecast()

    count = 0
    for w in f:
        results['forecast'].append({})
        results['forecast'][count]
        results['forecast'][count]['location'] = location.get_name()
        results['forecast'][count]['time'] = w.get_reference_time(timeformat='iso')
        results['forecast'][count]['description'] = w.get_detailed_status()
        results['forecast'][count]['temperature'] = float("{0:.1f}".format(w.get_temperature()['temp']-273.15))
        results['forecast'][count]['temp_max'] = float("{0:.1f}".format(w.get_temperature()['temp_max']-273.15))
        results['forecast'][count]['temp_min'] = float("{0:.1f}".format(w.get_temperature()['temp_min']-273.15))
        #results['forecast'][count]['wind_direction'] = w.get_wind()['deg']
        results['forecast'][count]['wind_speed'] = w.get_wind()['speed']
        results['forecast'][count]['clouds'] = w.get_clouds()
        results['forecast'][count]['humidity'] = w.get_humidity()
        results['forecast'][count]['pressure'] = w.get_pressure()['press']
        results['forecast'][count]['sunrise_time'] = w.get_sunrise_time('iso')
        results['forecast'][count]['sunset_time'] = w.get_sunset_time('iso')
        count+=1

    return results

get_weather()
