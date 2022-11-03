import requests, json

kaupunki = input("Anna kaupungin nimi: ")
 
url = "http://api.openweathermap.org/data/2.5/weather?&lang=fi&appid=f0ff61054831cb76fbc9183599c5bfef&q=" + kaupunki + "&units=metric"

x = requests.get(url).json()

try: 
    lämpötila = x["main"]["temp"]
    desc = x["weather"][0]["description"]
    
    print(f"{desc} lämpotila on {lämpötila}°c")
except:
    print("Hakua ei voinut suorittaa")