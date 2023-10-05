
import requests

#& the api endpoint(address of data you want to get) goes into the url variable


response = requests.get(url="http://api.open-notify.org/iss-now.json") #an api request

response.raise_for_status() #will raise the specific error code if the url not found


data = response.json()
iss_position_only = data["iss_position"]
longitude_only = iss_position_only["longitude"];
latitude_only = iss_position_only["latitude"];

# print(f" this is the current ISS Position: {iss_position_only}")
# print(f" this is the current ISS Position's longitude: {longitude_only}")
# print(f" this is the current ISS Position's latitude: {latitude_only}")

print(f"Latitude: {latitude_only} | Longitude: {longitude_only}")


##Response codes:
#$Summary
#! status codes references(more detailed): "https://www.webfx.com/web-development/glossary/http-status-codes/"
#* 1xx: Hold on
#* 2xx: successful
#* 3xx: you dont have permission
#* 4xx: the user made a mistake
#* 5xx: the server made a mistake  