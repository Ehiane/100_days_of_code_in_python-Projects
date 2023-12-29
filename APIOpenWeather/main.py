import requests

OPEN_WEATHER_API_KEY = "8e1d5526f0043ed22ac192a0ab51478e" # got it from registering from the website

position = (47.479694, -122.207924) # latitude, longitude 

parameters = {
    'lat': position[0],
    'lon': position[1],
    'appid': OPEN_WEATHER_API_KEY,
    'cnt': 4 # happens every 3 hrs, 4*3 = 12hrs
}

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=api_endpoint, params = parameters)
try:
    print(f"status code : {response.status_code}")
    weather_data = response.json()
    # print(weather_data)
except response.status_code != 200:
    response.raise_for_status()



# link for weather conditions code: "https://openweathermap.org/weather-conditions"
    
def check_weather_condition(json_weather_data):    
    for each_interval_dict in  json_weather_data['list']:
        if each_interval_dict['weather']:
            inner_dict = each_interval_dict['weather'][0]
            # print(inner_dict)
            id, brief_description, description = inner_dict['id'] ,inner_dict['main'],inner_dict['description']
            print(f'id: {id}, description: {description}')
            if id < 700: 
                print('Bring an umbrella')
            else:
                print('No need to bring an umbrella')


check_weather_condition(weather_data)





