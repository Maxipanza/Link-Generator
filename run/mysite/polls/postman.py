import requests
import json

url = "http://181.97.199.115:25565/"

payload = json.dumps("enviado desde visual")
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
