import requests
import json
url = "https://api.heygen.com/v2/photo_avatar/look/generate"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "<API KEY>"
}
payload = {  
     "group_id": "57775a7e02664fcda467a16fd8a9059e", 
  "flow_id": "f9e58c96b86240aab05543942051a2e4",
  "name": "36f9bca47f0c401faed22aa2d435b7f2",
  "gender": "Woman", 
  "age": "Young Adult", 
  "ethnicity": "White",
  "prompt": "White shirt front-facing",
  "orientation": "square",
  "pose": "full_body",
  "style": "Realistic"
}

response = requests.post(url, json=payload, headers=headers)

print(json.dumps(response.json(), indent=2))
