import json
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://api.bluelytics.com.ar/v2/latest')
    response.raise_for_status
    jsonResponse = response.json()
    blacklist = ['last_update'] ##aca
    ##print("print cada key")
    for key, value in jsonResponse.items():
        if key not in blacklist:
            print(key, ":", value['value_avg'])
        else:
            print("no se que esta pasando")

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Ocurrio otro error: {err}')