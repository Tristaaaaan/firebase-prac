import requests
import json

firebase_url = 'https://login-e4383-default-rtdb.asia-southeast1.firebasedatabase.app/.json'


json_data = {"url": "amazon.com", "age": "15"}

res = requests.patch(url=firebase_url, json=json.loads(json_data))

print(res)
