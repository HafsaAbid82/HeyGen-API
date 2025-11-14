import requests
import json
url = "https://api.heygen.com/v2/photo_avatar/add_motion"

payload = { "motion_type": "consistent",
          "id":"57775a7e02664fcda467a16fd8a9059e",
            }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "<API KEY>"
}

response = requests.post(url, json=payload, headers=headers)

print(json.dumps(response.json(), indent=2))
