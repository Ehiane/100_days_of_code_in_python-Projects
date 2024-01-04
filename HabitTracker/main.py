import requests,os

USERNAME = 'ehiane'
TOKEN = os.environ.get("PIXELA_USER_TOKEN")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
    # 'thanksCode': ..., #optional
}

## Created account by calling this(don't call it more than once)
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    'id':...,
    'name':...,
    'unit':...,
    'type':...,
    'color':...,
}

requests.post()

