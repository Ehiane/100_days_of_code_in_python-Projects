import os
import requests
from twilio.rest import Client


# ---------------------------------------[Twilio messaging API part]-----------------------------------
# downloaded 'twilio' library
# saving confidentials as environment variables

TWILIO_RECOVERY_CODE = os.environ.get('TWILIO_RECOVERY_CODE')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

# ---------------------------------------[(OWM)Open Weather Map API part]-----------------------------------
## to save an environment variable in cmd : 'set <variablename>=<value>' or DO IT MANUALLY, IF IT DOESNT WORK
## to check environment variables: 'dir ENV:'. Restart vscode if it doesent show up immediatly.

OWM_API_KEY = os.environ.get('OWM_API_KEY') # got it from registering from the website 
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
position = (48.173960, -117.017280) # latitude, longitude 
parameters = {
    'lat': position[0],
    'lon': position[1],
    'appid': OWM_API_KEY,
    'cnt': 4 # happens every 3 hrs, 4*3 = 12hrs
}
response = requests.get(url=OWM_API_ENDPOINT, params = parameters)
try:
    print(f"status code : {response.status_code}")
    weather_data = response.json()
    # print(weather_data)
except response.status_code != 200:
    response.raise_for_status()


# link for weather conditions code(id): "https://openweathermap.org/weather-conditions"
def check_weather_condition(json_weather_data):
    print('ran')    
    for each_interval in  json_weather_data['list']:
        if isinstance(each_interval['weather'],dict):
            weather_details = each_interval['weather'][0] # 0, because there is always only one element in the list
            id, description = weather_details['id'] ,weather_details['description']
            if will_rain(weather_code=id): 
              print("queued")
              text = f"It's going to rain today☔!Bring an umbrella!\nWeather Forcast:{description}"
              message = client.messages \
                .create( # the '\' above is used for code line continuation in python, in order to separate code on different lines without a syntax error.
                     body=f"{text}",
                     from_=TWILIO_PHONE_NUMBER,
                     to='+14258660288'
                )
              print(message.status) 
            else:
              print("queued")
              text = f"It's not going to rain today🌤️!No need to bring an umbrella!\nWeather Forcast:{description}"
              message = client.messages \
                .create( # the '\' above is used for code line continuation in python, in order to separate code on different lines without a syntax error.
                     body=f"{text}",
                     from_=TWILIO_PHONE_NUMBER,
                     to='+14258660288'
                )
              print(message.status) 

def will_rain(weather_code):
    return True if weather_code > 700 else False

#! Twilio is experiencing toll free number shutdown as of nov 8 2023. So it is not working.
check_weather_condition(weather_data) 