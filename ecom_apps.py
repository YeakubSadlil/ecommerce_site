import requests
import json

def get_data(id=None):
    params = {}
    if id is not None:
        params['id'] = id
    r = requests.get('http://127.0.0.1:8000/users/',params=params)
    try:
        data = r.json()
        print(f"Username : {data[0].get('username', 'No username available')} \nemail : {data[0].get('email', 'email is not available')}")
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode json")

get_data(6)