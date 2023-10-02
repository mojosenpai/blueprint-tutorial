import requests
import json

data = requests.get('http://127.0.0.1:5000/api/all').text
parsed = json.loads(data)
print(parsed['data'])