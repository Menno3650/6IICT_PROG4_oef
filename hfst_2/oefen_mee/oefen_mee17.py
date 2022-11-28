import json, requests # Benodigde modules

""" STAP 1: API klaarmaken om JSON in string-formaat te downloaden """
# Geef tweeletter-code van land (https://www.iban.com/country-codes)
land = input("Geef tweeletter-code van land (Belgie = BE): ")
# Geef stad:
stad = input(f"Geef stad (in het Engels): ")
# Geef API-key:
API_key = "VUL ZELF IN"

# Stel de api op, waarmee we data kunnen afhalen van openweathermap.org
api = f"https://api.openweathermap.org/data/2.5/forecast?q={stad},{land}&appid={API_key}"

""" STAP 2: Haal JSON-string af van OpenWeatherMap.org """
# Roep weerdata op via api.
antwoord = requests.get(api).text

# Haal uit commentaar om onbewerkte JSON text te zien.
# print(antwoord) 

""" Stap 3: Vorm JSON-string om naar Python structuur (lijst of dictionary). 
       Tip: Schrijf structuur weg naar JSON-bestand, je kan deze gebruiken voor stap 4. 
"""


""" Stap 4: Print weerbeschrijving op basis van structuur 
       Tip: analyseer hiervoor de verkregen data. 
            Welke structuren zijn aanwezig? Via welke keys/index krijg ik de benodigde data?
"""