from itertools import count
import json
from urllib import response
import requests
from requests.exceptions import HTTPError

'''

def dolar():

    try:
        response = requests.get('https://api.bluelytics.com.ar/v2/latest')
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        for key, value in jsonResponse.items():
            if (key != "last_update" and key == "oficial"):
             #print(int(value['value_avg']))
             return int(value['value_avg'])
                
        
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

dolar()

'''

class claseDolar:
    def __init__(self):
        try:
            self.response = requests.get('https://api.bluelytics.com.ar/v2/latest')
            self.response.raise_for_status()
            # access JSOn content
            self.jsonResponse = self.response.json()
        
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def oficial(self):
        for key, value in self.jsonResponse.items():
            if (key != "last_update" and key == "oficial"):
                return int(value['value_avg'])

    def blue(self):
        for key, value in self.jsonResponse.items():
            if (key != "last_update" and key == "blue"):
                return int(value['value_avg'])



class apiFer:
    def __init__(self):
        self.url = "http://181.97.199.115:25565/"
    def postVal(self):
        valor=input("ingrese valor a enviar:")
        try:
            payload = json.dumps(valor)
            headers = {
  'Content-Type': 'application/json'
}
            response = requests.request("POST", self.url, headers=headers, data=payload)
            response.raise_for_status()
            print(response)
        
        except HTTPError as http_err: 
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')





apiFer().postVal()

#print(claseDolar().blue())
#print(claseDolar().oficial())