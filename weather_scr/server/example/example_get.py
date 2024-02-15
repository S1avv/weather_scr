import requests
import json

data = "New York"

response = requests.get(f"http://127.0.0.1:8000/weather/{data}").json()

print(json.dumps(response, indent=3))