import os, requests, datetime, pytz
# pytz used for timezones

## find result here: https://docs.google.com/spreadsheets/d/1et4lJuoWkZfeDYQ2c95g9vry4qeHUGPlimMSXVAU1DE/edit#gid=512663232

# ------------------------------------------[Nutritionix Setup]--------------------------------------------------------------
"""
Nutrionix is a language model that takes in text and deciphers the potential outcome of a workout in
from that text. It may return potential calories burned, potenial duration of the exercise, etc.
"""
NUTRIRIONIX_APP_ID = os.environ.get("NUTRIRIONIX_APP_ID")
NUTRIRIONIX_API_KEY = os.environ.get("NUTRIRIONIX_API_KEY")
NUTRIRIONIX_API_EXERCISE_ENDPOINT = (
    "https://trackapi.nutritionix.com/v2/natural/exercise"
)

nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRIRIONIX_APP_ID,
    "x-app-key": NUTRIRIONIX_API_KEY,
}

user_query = input("What exercises did you do? :")
nutrionix_parameters = {
    "query": user_query,
    "age": 20,
    "weight_kg": 75,
    "height_cm": 179.705,
}
nutritionix_response = requests.post(
    url=NUTRIRIONIX_API_EXERCISE_ENDPOINT,
    json=nutrionix_parameters,
    headers=nutritionix_headers,
)
try:
    if nutritionix_response.json() != {} or len(nutritionix_response.json()['exercises'][0]) > 0: # if the response isn't empty
        exercise_analysis = nutritionix_response.json()
        print(exercise_analysis)
except nutritionix_response.status_code != 200:
    nutritionix_response.raise_for_status()


# ---------------------------------[JSON STRUCTURE] -------------------------------------------------
"""
{'exercises': 
[   {'tag_id': 766, 'user_input': 'dumbell', 'duration_min': 1, 'met': 3.5, 'nf_calories': 4.38, 
    'photo': {
            'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_highres.jpg', 
            'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_thumb.jpg', 
            'is_user_uploaded': False
            }, 
    'compendium_code': 2054, 'name': 'weight lifting', 'description': None, 'benefits': None
    }, 
    {
    'tag_id': 766, 'user_input': 'press', 'duration_min': 15, 'met': 3.5, 'nf_calories': 65.63, 'photo': 
    {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_highres.jpg', '
    thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_thumb.jpg', 'is_user_uploaded': False}, 
    'compendium_code': 2054, 'name': 'weight lifting', 'description': None, 'benefits': None}]}
"""


# ------------------------------------------[Sheety Setup]--------------------------------------------------------------
"""
Sheety is a spreadsheet api that specifically modifies google sheets. 
You can insert, delete, edit columns and rows.
"""
# SHEETY_API_ENDPOINT = "https://api.sheety.co/phill/myWebsite/emails"
SHEETY_API_ENDPOINT = (
    "https://api.sheety.co/0ac3633618478475acdbb3fe273f2b4b/myWorkouts/workouts"
)

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
SHEETY_AUTH_CODE = os.environ.get("SHEETY_AUTH_CODE")

print(SHEETY_USERNAME,SHEETY_PASSWORD,SHEETY_AUTH_CODE)

sheety_auth_headers = {
    "Authorization": SHEETY_AUTH_CODE,
    "Content-Type": "application/json",
}


def get_todays_date_and_time() -> str:
    # date section
    today_date = datetime.datetime.now()
    today_date_str = today_date.strftime(r"%A %d of %B, %Y")  # %A dayName, %B monthName

    # time section
    current_utc_time = datetime.datetime.utcnow()
    pullman_timezone = "America/Los_Angeles"
    pullman_timezone_obj = pytz.timezone(pullman_timezone)
    current_time_in_pullman = current_utc_time.replace(tzinfo=pytz.utc).astimezone(
        pullman_timezone_obj
    )

    current_time_in_pullman = current_time_in_pullman.strftime(
        "%I:%M %p"
    )  # %I 12hr clock format, %M minute , %p am or pm

    return today_date_str, current_time_in_pullman

DATE, TIME = 0, 1
workout_row = {
    "workout": {
        "date": get_todays_date_and_time()[DATE],
        "time": get_todays_date_and_time()[TIME],
        "exercise": exercise_analysis['exercises'][0]['user_input'],
        "duration": exercise_analysis['exercises'][0]['duration_min'],
        "calories": exercise_analysis['exercises'][0]['nf_calories'],
        "category": exercise_analysis['exercises'][0]['name'],
        "description": user_query,
    }
}

sheety_response = requests.post(url=SHEETY_API_ENDPOINT,json=workout_row,headers=sheety_auth_headers)
try:
    print(sheety_response.json())
except sheety_response.raise_for_status():
    print(sheety_response.status_code)


# ------------------------------------------[Resources]--------------------------------------------------------------
"""
Here is a list of all the crucial resources used for the development of this mini-project.
"""
RESOURCES = {
    # sheety - spreadsheet API
    'sheetyDashboard': 'https://dashboard.sheety.co/projects/65a4c2caec339004d7c57fb0/auth',
    'sheetyRequestsDocumentation': 'https://sheety.co/docs/requests.html',
    'sheetyAPIDocumentaion': 'https://dashboard.sheety.co/projects/65a4c2caec339004d7c57fb0/sheets/workouts',
    
    # nutirionix - natural Language for excerice (ChatGPT of Excerices)
    'nutritionixDocumentation': 'https://developer.syndigo.com/docs/nutritionix-api-guide',
    'nutritionixAccountDetails': 'https://developer.nutritionix.com/admin/access_details',
    'nutriionixNaturalLanguageForExcerciseDocumentation': 'https://developer.syndigo.com/docs/natural-language-for-exercise'
}