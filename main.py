import requests
import json
from pprint import pprint

token = '1693418503:AAEcpgl164M2nl0HXzwk0EbnPqnttI3gzmQ'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
pprint(data)
updates = data['result']
print(updates)