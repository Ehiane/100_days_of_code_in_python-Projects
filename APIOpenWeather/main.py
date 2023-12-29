import requests

OPEN_WEATHER_API_KEY = "8e1d5526f0043ed22ac192a0ab51478e" # got it from registering from the website

position = (47.479694, -122.207924) # latitude, longitude 

parameters = {
    'lat': position[0],
    'lon': position[1],
    'appid': OPEN_WEATHER_API_KEY
}

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=api_endpoint, params = parameters)
try:
    print(f"status code : {response.status_code}")
    api_data = response.json()
    print(api_data)
except :
    response.raise_for_status()





