import requests
url = "https://upload.heygen.com/v1/asset"
headers = {
    "accept": "application/json",
    "Content-Type": "image/jpeg",
    "X-API-KEY": "<API KEY>"
}
with open("test.png", "rb") as img:
    data = img.read()
    
response = requests.post(url, headers=headers, data=data)

print(response.text)
