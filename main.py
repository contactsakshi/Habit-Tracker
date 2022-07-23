import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'sakshicodes'
TOKEN = 'dwjncbcherbve'
GRAPH_ID = 'meditate2day2'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes',
}
#creating a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#creatign a graph definition

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    'id': GRAPH_ID,
    'name' : 'Meditation Graph',
    'unit':   'commit',
    'type': 'int',
    'color': 'shibafu',

}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers )
# print(response)

#posting pixels

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input('Did you meditate today. Type 0 for no or 1 for yes'),
}

p_headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=p_headers)
# print(response.text)