import requests, json

client_id = "7e03a450791d4176b9205da294af329e"
client_secret = "6fdbb6ec953e4b67a27664d7aa31f264"

# Herinner je dat een API gewoon een speciale URL is...
# Via deze URL kunnen we ons inlogtoken aanvragen.
url = 'https://accounts.spotify.com/api/token'

# Deze zaken moeten we de API geven om een inlogtoken te genereren.
inloggegevens = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# requests het inlogtoken, haal de tekst uit deze request en zet in cred_response
cred_resp = requests.post(url, inloggegevens).text
# Opgelet! Onderstaande regel is BELANGRIJK. 
cred_resp = json.loads(cred_resp)

print(cred_resp)

""" Oefen mee 2: 
zet de dictionary cred_resp in JSON-bestand met de naam certificatie.json

"""