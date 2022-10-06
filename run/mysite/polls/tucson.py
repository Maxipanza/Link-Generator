import json
import requests
from requests.exceptions import HTTPError

def apiFer():
    try:
        url = "http://181.97.199.115:25565/"
        payload = json.dumps("enviado desde visual con una funcion")
        headers = {
  'Content-Type': 'application/json'
}
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


apiFer()