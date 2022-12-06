import json
import requests
import os

KEY = os.environ["APIKEY"]
URL_FIND = os.environ["URL_FIND"]
URL_INSERT = os.environ["URL_FIND"]

def CRUD(url, payload):
    
    url = url

    payload = payload

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': KEY,
        'Accept': 'application/json'
        }
    
    try:
        query = requests.post(url, headers=headers, data=payload)
        status = query.status_code
        query.raise_for_status()
        
    except requests.exceptions.HTTPError:

        if status == 400:
            print("The query isn't correct")

        if status == 401:
            print("Unauthorized user tries to connect!")
        
        if status == 404:
            print("HTTP not found!")

        if status == 500:
            print("Internal server error")
    
    else:

        print("Successful connection!") 
       
