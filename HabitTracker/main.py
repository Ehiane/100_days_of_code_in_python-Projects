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
    'id':"ehianegraph1",
    'name':"Coding Graph",
    'unit':"hour",
    'type':"int",
    'color':"ajisai",
}

headers = {
    'X-USER-TOKEN':TOKEN,
}

MY_GRAPH_URL = f"https://pixe.la/v1/users/{graph_params['name']}/graphs/{graph_params['id']}.html"

response = requests.post(url=GRAPH_ENDPOINT,json=graph_params, headers= headers)
print(response.text)
