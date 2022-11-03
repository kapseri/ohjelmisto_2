import json
import requests



pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()
try:
    print(json.dumps(vastaus["value"], indent=2))
except:
    print("Hakua ei voinut suorittaa")