import requests

# Welke webpagina doorzoeken?
URL = "VUL AAN" 
# Wat moet een HTML regel bevatten om een hit te zijn?
# Er is in dit geval gezocht naar links & andere webpagina's.
hits = ["<a", ".php", ".html", "href"]

# Haal alle HTML-code van de webpagina af.
response = requests.get(URL).text
# Splits op in lijst op basis van "\n"
webpage = response.split("\n")

# Voor iedere lijn code op de webpagina
for line in webpage:
    # Als de lijn een hit-woord bevat... Print de lijn!
    if any([True for hit in hits if hit in line]): 
        print("Hit gevonden: ")
        print(line.strip())                             
        print("-"*30)