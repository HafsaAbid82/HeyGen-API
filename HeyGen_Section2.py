import requests
import json
Motion_url = "https://api.heygen.com/v2/photo_avatar/add_motion"

payload = { "motion_type": "consistent",
          "id":"7a0fc3dd5f10494ca09dcb2cf0d65725",
            }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "sk_V2_hgu_kVoJliPAd1a_1GdyDLm6D2NGefqwEuqejLfoMwdIBgjw"
}
Motion = requests.post(Motion_url, json=payload, headers=headers)
response = Motion.json()
id = response["data"]["id"] 
Sounds_url = "https://api.heygen.com/v2/photo_avatar/add_sound_effect" 
data = {  
     "id": id, 
  }
response = requests.post(Sounds_url, json=data, headers=headers)
print("Motion and Sounds Added Successfully")