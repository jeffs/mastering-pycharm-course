import requests
import toml

# import sqlalchemy

static = toml.load("static.toml")

resp = requests.get(static["url"])
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']

print(f"hello world, it's {temp} outside!")
