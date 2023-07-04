import json
import requests
import sys


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif not (sys.argv[1]).isnumeric():
    sys.exit("Command-line argument is not a number")


try:
    # Send a GET request to the Coindesk API
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Print the JSON data with indentation for readability
        # print(json.dumps(data, indent=2))

        # Extract the USD float price from the JSON data
        usd_price = float(data['bpi']['USD']['rate_float'])

        # Print the USD float price
        total = usd_price * float(sys.argv[1])
        print(f"${total:,.4f}")
    else:
        # Print an error message if the request was unsuccessful
        print("Error: Failed to retrieve data from the API.")

except requests.RequestException as e:
    # Print an error message if there was an exception during the request
    print("Error:", str(e))
