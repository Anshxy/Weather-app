import requests, json
 

def get_weather(w):
    """ 
    Get weather data 
    """
    
    
    t = w["main"]["temp"]
    f = w["main"]["feels_like"]
    max = w["main"]["temp_max"]
    min = w["main"]["temp_min"]

    basic_description = w["weather"][0]["description"]

    # meter/second
    wind_speed = w["wind"]["speed"]

    # degrees meteorogical
    wind_deg = w["wind"]["deg"]

    place = w["sys"]["country"]

    # Measurement is Kelvin so we use a formula to convert it to celcius
    celcius = t - 273.15
    mx = max - 273.15
    mn = min - 273.15
    feels = f - 273.15

    return basic_description, place, celcius, mx, mn, feels


    








 

