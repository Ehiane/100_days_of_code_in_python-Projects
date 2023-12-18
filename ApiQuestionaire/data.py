import requests

API_URL = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
parameters = {
    'amount': 10,
    'type': 'boolean'
}

data = None
try:
    response = requests.get(API_URL)
    data = response.json()
except:
    response.raise_for_status()

question_data = data['results']
