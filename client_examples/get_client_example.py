import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/1"
headers = {"Content-Type": "application/json"}
response = requests.get(API_URL, headers=headers)
response.json()

print(response.json())
