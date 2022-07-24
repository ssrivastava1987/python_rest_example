import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type": "application/json"}
response = requests.post(api_url, json=todo, headers=headers)
response.json()
print(response.json())
