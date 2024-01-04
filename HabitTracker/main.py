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
GRAPH_ID = "ehianegraph1"
graph_params = {
    'id': GRAPH_ID,
    'name':"Coding Graph",
    'unit':"hour",
    'type':"int",
    'color':"ajisai",
}

headers = {
    'X-USER-TOKEN':TOKEN,
}

## Created graph by calling this(don't call it more than once)
# response = requests.post(url=GRAPH_ENDPOINT,json=graph_params, headers= headers)
# print(response.text)

## the result of the graph post:
MY_GRAPH_URL = f"https://pixe.la/v1/users/ehiane/graphs/ehianegraph1.html" #click this to view my graph

# a pixel is a cell on the graph
pixel_params = {
    'date': '20240104', # has to be in the format yyyyMMdd
    'quantity': '1', # since  i specified mine to be in int, it has to be str(int)
}

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=PIXEL_CREATION_ENDPOINT,json=pixel_params,headers=headers)
print(response.text) 




