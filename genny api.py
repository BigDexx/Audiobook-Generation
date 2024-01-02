import requests

file = open('D:\Coding Work\Codeforces\Python\Reddit.txt','r')
t = ((file.read(500)))
print(t)
file.close()

url = "https://api.genny.lovo.ai/api/v1/tts/sync"

payload = {
    "speed": 1,
    "speaker": "640f477d2babeb0024be422b",
    "text": t
}
headers = {
    "accept": "application/json",
    "content-type":  "application/json",
    "X-API-KEY": "9d9e57c1-7cb4-457d-ad9b-955a2b646dbe"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

