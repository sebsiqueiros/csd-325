import requests
import json

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

print("STATUS CODE:")
print(response.status_code)

data = response.json()

print("\nRAW RESPONSE:")
print(data)

print("\nFORMATTED RESPONSE")
print("-" * 40)

print("Setup:")
print(data["setup"])

print("\nPunchline:")
print(data["punchline"])

