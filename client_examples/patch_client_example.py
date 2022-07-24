import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
headers = {"Content-Type": "application/json"}
response = requests.patch(api_url, json=todo, headers=headers)
response.json()
