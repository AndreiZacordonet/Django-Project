# import requests
#
# url = "http://localhost:8000/api/location/"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

import requests
import json

url = "http://localhost:8000/api/location/"

payload = json.dumps({
  "city": "Timisoara32",
  "country": "Romania"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

response = requests.request("POST", "http://localhost:8000/api/locations/5/update/", headers=headers, data=payload)

print(response.text)