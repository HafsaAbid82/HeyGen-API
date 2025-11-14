import requests
url = "https://upload.heygen.com/v1/asset"
headers = {
    "accept": "application/json",
    "Content-Type": "image/jpeg",
    "X-API-KEY": "sk_V2_hgu_krGIQx04mA4_sdhZhRRAFPV3nLq5HVNx3uDWTS7swTNG"
}
with open("test.png", "rb") as img:
    data = img.read()
    
response = requests.post(url, headers=headers, data=data)

print(response.text)