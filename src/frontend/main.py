import requests

endpoint = 'http://127.0.0.1:8000/api/?abs=123'

r = requests.get(endpoint, json={"msg": 'Hello world'})


print(r.json())