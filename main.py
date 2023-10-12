import requests;
import webbrowser;

key = '9uczFinrDl5mRKIXAwrn8NO7Zp4g8aj2'

url = 'https://www.mapquestapi.com/geocoding/v1/address?key='

location = input("Scegli la localizzazione da cercare: ")

main_url = url + key + '&location=' + location

r = requests.get(main_url)

data = r.json()['results'][0]
loc = data['locations'][0]

latitude = loc['latLng']['lat']
longitude = loc['latLng']['lng']

print(loc)

google_maps_url = f'https://www.google.com/maps?q={latitude},{longitude}'

print("Google Maps URL:", google_maps_url)

webbrowser.open(google_maps_url)
