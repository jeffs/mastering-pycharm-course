import requests
import toml

# import sqlalchemy


resp = requests.get(**toml.load("request.toml"))
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']

print(f"The outdoor temperature is {temp}º F.")
