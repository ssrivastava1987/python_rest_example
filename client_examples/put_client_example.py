import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()

todo = {"userId": 1, "title": "Wash car", "completed": True}
headers = {"Content-Type": "application/json"}
response = requests.put(api_url, json=todo, headers=headers)
response.json()
print(response.json())
