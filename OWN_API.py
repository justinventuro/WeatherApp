import urllib
from urllib import parse
import requests

def own_api_call(address):


    main_API = 'http://api.openweathermap.org/data/2.5/weather?'
    key = 'f2bd2c935addeed759e69729e76a9957'

    url = main_API + urllib.parse.urlencode({'q': address['area']}) + "&units=metric" + "&appid=" + key

    json_data = requests.get(url).json()
    api_status_code = json_data['cod']

    if api_status_code == 200:
        weather ={
            'location' : json_data['name'],
            'weather_description' : json_data['weather'][0]['description'],
            'weather_temperature' : json_data['main']['temp'],
            'icon': json_data['weather'][0]['icon']

        }
        weather['formatted_address']=address['formatted_address']

    return weather
