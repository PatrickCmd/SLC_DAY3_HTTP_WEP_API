'''Public RESTAPI using python'''

# Import the modules
import requests
import json

# Make it a bit prettier..
print("-" * 100)
print("This will show list of countries, all the county name, 2 character code and 3 character assigned code.")
print("-" * 100)

# Get the feed
r = requests.get("http://services.groupkt.com/country/get/all")
result = r.text

# Convert it to a Python dictionary
# data = json.loads(r.text)
print(result)