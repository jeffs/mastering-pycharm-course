import requests
import toml

# import sqlalchemy

data = toml.load("./data.toml")

resp = requests.get(data["url"])
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']

print(f"hello world, it's {temp} outside!")
