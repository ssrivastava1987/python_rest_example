import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
headers = {"Content-Type": "application/json"}
response = requests.get(api_url, headers=headers)
response.json()

print(response.json())
