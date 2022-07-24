import requests

API_URL = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type": "application/json"}
response = requests.post(API_URL, json=todo, headers=headers)
response.json()
print(response.json())
