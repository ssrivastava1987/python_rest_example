import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(API_URL)
response.json()
print(response.json())
