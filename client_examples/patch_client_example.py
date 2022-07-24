import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
headers = {"Content-Type": "application/json"}
response = requests.patch(API_URL, json=todo, headers=headers)
response.json()
