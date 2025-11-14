import requests
import json
url = "https://api.heygen.com/v2/photo_avatar/avatar_group/create"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "<API KEY>"
}
payload = {
    "id": "36f9bca47f0c401faed22aa2d435b7f2",
    "image_key": "image/36f9bca47f0c401faed22aa2d435b7f2/original", 
    "name": "36f9bca47f0c401faed22aa2d435b7f2",
}

response = requests.post(url, json= payload, headers=headers)

print(json.dumps(response.json(), indent=2))
