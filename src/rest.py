import json

import requests

# THIS WORKS!!!!
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

# r = requests.post(url, data=json.dumps(payload), headers=headers)
r = requests.get(url)
print("r.text = ", r.text)
print("r.json() = ", r.json().get('message'))
