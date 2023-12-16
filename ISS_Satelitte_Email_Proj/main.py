#Response codes: status codes references(more detailed): "https://www.webfx.com/web-development/glossary/http-status-codes/"
#* 1xx: Hold on
#* 2xx: successful
#* 3xx: you dont have permission
#* 4xx: the user made a mistake
#* 5xx: the server made a mistake  
## the api endpoint(address of data you want to get) goes into the url variable

import requests

SUNSET_SUNRISE_API = "https://api.sunrise-sunset.org/json"
POSITION = (46.729721,-117.181831) #latitude, longitude
# ----------------------------------------[API Basics]------------------------------------------------

# response = requests.get(url="http://api.open-notify.org/iss-now.json") #an api request
# response.raise_for_status() #will raise the specific error code if the url not found
# data = response.json()
# iss_position_only = data["iss_position"]
# longitude_only = iss_position_only["longitude"];
# latitude_only = iss_position_only["latitude"];

# print(f" this is the current ISS Position: {iss_position_only}")
# print(f" this is the current ISS Position's longitude: {longitude_only}")
# print(f" this is the current ISS Position's latitude: {latitude_only}")

# ----------------------------------------[API Parameters]------------------------------------------------
parameters = {
    'lat': POSITION[0],
    'lng': POSITION[1],
    'formatted': 0,
}


#strip whitespace when implementing
## URL syntax = "<https_link aka end_point> ? <parameter> = <value>& ... "
#example = "https://api.sunrise-sunset.org/json?lat=46.729721&lng=-117.181831" 

if __name__ == '__main__':
    # print(f"Latitude: {latitude_only} | Longitude: {longitude_only}")
    api_response = requests.get(SUNSET_SUNRISE_API, params=parameters)
    if api_response.status_code == 200:
        data = api_response.json()
        sunrise = data.get('results').get('sunrise').split('T')[1].split(":")
        sunrise_hour = sunrise[0]
        sunset = data.get('results').get('sunset').split('T')[1].split(":")
        sunset_hour = sunset[0]
        print(f"sunrise hour: {sunrise_hour}, sunset hour: {sunset_hour}")
        print(f"Sunrise:{sunrise} \nSunset:{sunset}.\nin the UK as regards to Pullman.")
    else:
        api_response.raise_for_status()
    ...
