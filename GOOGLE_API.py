import urllib
import requests
from urllib import parse


def g_api_call(address):
    g_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
    key = 'AIzaSyDRjPNMDlQisJ5fbUU4M_6-BH-qdi4fwk0'

    url_main = g_api + urllib.parse.urlencode({'address': address, 'key': key})

    json_data_main = requests.get(url_main).json()
    api_status = json_data_main['status']


    if api_status == 'OK':
        count = 0
        formatted_address = json_data_main['results'][0]['formatted_address']
        for each in json_data_main['results'][0]['address_components']:

            types = each['types'][0]

            if types == "locality":
                area = json_data_main['results'][0]['address_components'][count]['long_name']
                break
            count += 1

        google_data ={
            'formatted_address' : formatted_address,
            'area' : area
        }

        return google_data



