import requests
from twilio.rest import Client


# ---------------------------------------[Twilio messaging API part]-----------------------------------
# downloaded 'twilio' library
# saving confidentials as environment variables

TWILIO_RECOVERY_CODE = "37N8MFS6M9XF7L7BD9RYXV8K"
TWILIO_PHONE_NUMBER = "+18559430941"
TWILIO_ACCOUNT_SID = "AC1cb54a87eacc507a3575ba70f5d1db55"
TWILIO_AUTH_TOKEN = "8fbc006476238028e7ce38bb0c114e1c"
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

# ---------------------------------------[(OWM)Open Weather Map API part]-----------------------------------
# to save an environment variable in cmd : 'set <variablename>=<value>'
# to check environment variables: 'dir ENV:'
OWM_API_KEY = "8e1d5526f0043ed22ac192a0ab51478e" # got it from registering from the website 
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


check_weather_condition(weather_data) # Twilio is experiencing toll free number shutdown as of nov 8 2023. so it is not working
