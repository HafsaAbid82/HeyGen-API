import requests
import json
url = "https://api.heygen.com/v2/photo_avatar/train"

payload = {
    "id": "36f9bca47f0c401faed22aa2d435b7f2",
    "image_key": "image/36f9bca47f0c401faed22aa2d435b7f2/original", 
    "name": "36f9bca47f0c401faed22aa2d435b7f2",
    "group_id": "57775a7e02664fcda467a16fd8a9059e",
    "gender": "Woman", 
    "age": "Young Adult", 
    "ethnicity": "White", 
    "orientation": "square",
    "pose": "half_body",
    "style": "Realistic"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "sk_V2_hgu_krGIQx04mA4_sdhZhRRAFPV3nLq5HVNx3uDWTS7swTNG", 
}

response = requests.post(url, json= payload, headers=headers)

print(json.dumps(response.json(), indent=2))
