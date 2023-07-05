import json
import requests
import sys


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    print(json.dumps(response.json(), indent=2))


