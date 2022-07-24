import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(API_URL)
response.json()

todo = {"userId": 1, "title": "Wash car", "completed": True}
headers = {"Content-Type": "application/json"}
response = requests.put(API_URL, json=todo, headers=headers)
response.json()
print(response.json())
