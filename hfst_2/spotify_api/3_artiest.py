import requests, json, csv

""" Oefen mee 6:
Haal de dictionary op uit credentials.json.

Zet de waarde van de key "access_token" (de zeer lange string),
in de variabele wachtwoord. (Idem aan oefen mee 3)
"""

wachtwoord = "Vervang door waarde van de key 'access_token'."

""" Oefen mee 7:
Stel zelf de request op. Baseer je op voorgaande bestanden en de documentatie.
Alle info die de request nodig heeft, is reeds gegeven.
"""
headers = {
    "Authorization": f"Bearer {wachtwoord}"
}
artist_id = '15x1sKugh3vsyFDj5ooa0c'
url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=BE"

beste_liedjes = "Vervang door correcte request.get"
beste_liedjes = json.loads(beste_liedjes)

""" Oefen mee 8:
Zet de variabele lied in een JSON-bestand lied.json.

Welke artiest heb je net opgehaald?
"""

""" Oefen mee 9:
Vul de lijst van lijsten overzicht met info over de liedjes (baseer je op de header)
"""
overzicht = []
header = ["naam_lied", "lengte (sec)", "populariteit", "externe_url"]
overzicht.append(header)
for index, lied in enumerate(beste_liedjes["tracks"]):
    # Haal uit ieder lied de informatie beschreven in de header. Zet deze in lied_info.
    # De lijst lied_info wordt tenslotte toegevoegd aan het overzicht.
    print(lied) 
    lied_info = [] # Vul aan!
    overzicht.append(lied_info)

""" Oefen mee 10:
Maak een CSV-bestand beste_liedjes.csv aan op basis van het opgestelde overzicht.
"""