import requests
import json

url = "https://api.heygen.com/v2/photo_avatar/add_sound_effect"
headers = {
    "accept": "application/json",
    "x-api-key": ""<API KEY>""
}
payload = {  
     "id": "69e822924cc34dba9449d31e32ef0d63", 
  }

response = requests.post(url, json=payload, headers=headers)

print(json.dumps(response.json(), indent=2))
