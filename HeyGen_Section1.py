import requests
import json
Upload_Avatar_url = "https://upload.heygen.com/v1/asset"
header = {
    "accept": "application/json",
    "Content-Type": "image/png",
    "X-API-KEY":<API_Key>
}
with open("test.png", "rb") as img:
    data = img.read()
Upload_Avatar = requests.post(Upload_Avatar_url, headers=header, data=data)
response1 = Upload_Avatar.json()
Avatar_Group_url = "https://api.heygen.com/v2/photo_avatar/avatar_group/create"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "sk_V2_hgu_kVoJliPAd1a_1GdyDLm6D2NGefqwEuqejLfoMwdIBgjw"
}
image_key = response1["data"]["image_key"]   
id = response1["data"]["id"] 
name = response1["data"]["name"]  
data1 = {
    "id": id ,
    "image_key": image_key , 
    "name": name ,
}
Avatar_Group = requests.post(Avatar_Group_url, json= data1, headers=headers)
response2 = Avatar_Group.json()
group_id = response2["data"]["group_id"]    
Avatar_url = "https://api.heygen.com/v2/photo_avatar/train"
data2 = {
    "id": id,
    "image_key": image_key, 
    "name": name,
    "group_id": group_id,
    "gender": "Woman", 
    "age": "Young Adult", 
    "ethnicity": "White", 
    "orientation": "square",
    "pose": "half_body",
    "style": "Realistic"
}
Avatar = requests.post(Avatar_url, json= data2, headers=headers)
response3 = Avatar.json()
Looks_url = "https://api.heygen.com/v2/photo_avatar/look/generate"
data3 ={
    "group_id": group_id,
    "orientation": "square",
    "pose": "full_body",
    "style": "Realistic",
    "prompt": "Avatar smiling, with a clean background, high-resolution, natural lighting."
}
Looks = requests.post(Looks_url, json= data3, headers=headers)
response4 = Avatar.json()
print("Avatar Upload Completed Sucessfully.")

