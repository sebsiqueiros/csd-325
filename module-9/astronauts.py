import requests
import json

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("STATUS CODE:")
print(response.status_code)

data = response.json()

print("\nRAW RESPONSE:")
print(data)

print("\nCURRENT ASTRONAUTS IN SPACE")
print("-" * 40)

print("Number of astronauts:", data["number"])
print()

for person in data["people"]:
    print("Name:", person["name"])
    print("Craft:", person["craft"])
    print()
