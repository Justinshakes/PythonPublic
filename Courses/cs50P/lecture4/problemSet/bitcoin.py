import json
import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    argument = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a valid number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        usd_price = float(data['bpi']['USD']['rate_float'])
        total = usd_price * argument
        print(f"${total:,.4f}")
    else:
        print("Error: Failed to retrieve data from the API.")
except requests.RequestException as e:
    print("Error:", str(e))
