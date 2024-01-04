import requests, os, datetime

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

today = datetime.datetime.now().strftime(r'%Y%m%d')
date = today
# date = (today - datetime.timedelta(days=1)).strftime(r'%Y%m%d')  #  to customize date: datetime.datetime(year=..., month=... , day= ...).strftime(r'%Y%m%d')
# print(date)
# a pixel is a cell on the graph
pixel_params = {
    'date': datetime.datetime(year=2024,month=1,day=3).strftime(r'%Y%m%d'), # has to be in the format yyyyMMdd
    'quantity': '4', # since  i specified mine to be in int, it has to be str(int)
}

# PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=PIXEL_CREATION_ENDPOINT,json=pixel_params,headers=headers)
# print(response.text) 

## to update a pixel, use the put request
PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_params['date']}" 

pixel_update_params = {
    'quantity': '7',
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json= pixel_update_params, headers= headers)
# print(response.text) 


PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_params['date']}"
response = requests.delete(url=PIXEL_DELETE_ENDPOINT,headers=headers)
print(response.text)
