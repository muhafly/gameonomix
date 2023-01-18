import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"level": 2, "habit": 4})
print(get_response.json())
