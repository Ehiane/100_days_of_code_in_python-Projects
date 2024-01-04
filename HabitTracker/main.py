import requests,os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    'token': os.environ.get("PIXELA_USER_TOKEN"),
    'username': 'ehiane',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
    # 'thanksCode': ..., #optional
}


# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)