import requests, json

""" Oefen mee 3:
Haal de dictionary op uit credentials.json.

Zet de waarde van de key "access_token" (de zeer lange string),
in de variabele wachtwoord.
"""

wachtwoord = "Vervang door waarde van de key 'access_token'."

""" Oefen mee 4:
Vul url aan om de data van het lied op te halen.
"""
headers = {
    "Authorization": f"Bearer {wachtwoord}"
}
track_id = '6XnTftNvSj8mvYxoYB6a5j'
url = "Vervang door url van API."

lied = requests.get(url, headers=headers).text
lied = json.loads(lied)

""" Oefen mee 5:
Zet de variabele lied in een JSON-bestand lied.json.

Welk lied heb je net opgehaald?

Pas de dictionary aan door de keys "available markets" te verwijderen.
Schrijf de dictionary HIERNA pas weg naar een JSON-bestand.
"""
