import requests

from src.constants import NEEDED_VALUE

request_body = {'firstName': 'Rick'}
headers = {'Content-Type': 'application/json'}
method = "GET"
url_prepender = '{}'.format(NEEDED_VALUE)

resp = requests.get('{}{}'.format(url_prepender, method), headers=headers)
assert resp['ticket']['ticketId']
