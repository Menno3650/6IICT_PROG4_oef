#importeert alle modules die we gebruiken voor de gui
from tkinter import *
from tkinter.ttk import *
import tkintermapview                                
from ctypes import windll
import threading
import requests

#maakt het hele window aan genaamd root en de naam
root = Tk()
root.resizable(False, False)#zorgt dat het scherm niet gerezized kan worden
root.title('Space Project MZR')                     
windll.shcore.SetProcessDpiAwareness(True)#zet de resolutie scherper

#maakt de naam van de window aan
title = LabelFrame(root)
title.grid()

#hieroner worden de tabs aangemaakt
tabControl = Notebook(root)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)

#voegt alle tabs toe met de naam van iedere tab en voegt deze aan de grid
tabControl.add(tab1, text ='Space Stations')
tabControl.add(tab2, text ='GPS Satallites')
tabControl.add(tab3, text ='Starlink Satallites')
tabControl.add(tab4, text ='Weather Satallites')
tabControl.grid()

#krijgen de coordinaten van brussel door de long en lat te canverteren
brussel = tkintermapview.convert_address_to_coordinates("Brussel")

# Tab 1 voor commentaar zie Tab 4 onder aan de code
def add_marker_event1(coords):

    mapWidget1.delete_all_path()
    marker1.set_position(coords[0], coords[1])
    mapWidget1.set_path([brussel, coords])


progressLabel1 = Label(tab1,text = "Laden...")
progressLabelBar1 = Progressbar(tab1, orient= HORIZONTAL, length=600)
mapWidget1 = tkintermapview.TkinterMapView(tab1, height=400, width=600)
mapWidget1.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 
mapWidget1.set_zoom(0)    
mapWidget1.add_right_click_menu_command(label="Markeer Locatie",command=add_marker_event1,pass_coords=True)
locatie1 = mapWidget1.set_marker(brussel[0], brussel[1], text="Ik")
marker1 = mapWidget1.set_marker(1000.0, 1000.0, text="Locatie")


mapWidget1.grid(row = 0, column = 0, pady = 2)
progressLabelBar1.grid(row = 2, column = 0)



def apiThreadFunction1():
    response = requests.get("http://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=json")
    data = response.json()
    lengt = len(data)
    done = 0
    progressLabel1.grid(row = 1, column = 0, pady = 2)
    for item in data:
        name = item["OBJECT_NAME"]
        id = item["NORAD_CAT_ID"]
        response = requests.get(f"https://api.n2yo.com/rest/v1/satellite/positions/{id}/0.0/0.0/0/1&apiKey=DESUBF-GMFG7A-BS3C6F-4ZD5")
        satdata = response.json()
        lat = satdata["positions"][0]["satlatitude"]
        lon = satdata["positions"][0]["satlongitude"]
        done += 1
        mapWidget1.set_marker(lat, lon, text=name)
        print(f"[{done}/{lengt}] {name}: lat: {lat} lon: {lon}")
        progressLabel1.config(text = f"Laden: [{done}/{lengt}]")
        progressLabelBar1["value"] = (done/lengt)*100
    progressLabel1.config(text = f"Alles Is Geladen")
    progressLabelBar1.grid_remove()

# Tab 2 voor commentaar zie Tab 4 onder aan de code
def add_marker_event2(coords):
    mapWidget2.delete_all_path()
    marker2.set_position(coords[0], coords[1])
    mapWidget2.set_path([brussel, coords])

progressLabel2 = Label(tab2,text = "Laden...")
progressLabelBar2 = Progressbar(tab2, orient= HORIZONTAL, length=600)
mapWidget2 = tkintermapview.TkinterMapView(tab2, height=400, width=600)
mapWidget2.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite
mapWidget2.set_zoom(0)
mapWidget2.add_right_click_menu_command(label="Markeer Locatie",command=add_marker_event2,pass_coords=True)
locatie2 = mapWidget2.set_marker(brussel[0], brussel[1], text="Ik")
marker2 = mapWidget2.set_marker(1000.0, 1000.0, text="Locatie")


mapWidget2.grid(row = 0, column = 0, pady = 2)
progressLabelBar2.grid(row = 2, column = 0)

#maakt een nieuwe defenitie aan die helemaal apart loopt van het script en zorgt ervoor dat we alle api's krijgen van de tweede tab en de main loop blijft lopen. zoals de sattelieten
def apiThreadFunction2():
    response = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=gps-ops&FORMAT=json")
    data = response.json()
    lengt = len(data)
    done = 0
    progressLabel2.grid(row = 1, column = 0, pady = 2)
    #hier gaan we voor elke data da we hebben alle info er uithalen zoals long en lat
    for item in data:
        name = item["OBJECT_NAME"]
        id = item["NORAD_CAT_ID"]
        response = requests.get(f"https://api.n2yo.com/rest/v1/satellite/positions/{id}/0.0/0.0/0/1&apiKey=DESUBF-GMFG7A-BS3C6F-4ZD5")
        satdata = response.json()
        lat = satdata["positions"][0]["satlatitude"]
        lon = satdata["positions"][0]["satlongitude"]
        done += 1
        mapWidget2.set_marker(lat, lon, text=name)
        print(f"[{done}/{lengt}] {name}: lat: {lat} lon: {lon}")
        progressLabel2.config(text = f"Laden: [{done}/{lengt}]")
        progressLabelBar2["value"] = (done/lengt)*100
    progressLabel2.config(text = f"Alles Is Geladen")
    progressLabelBar2.grid_remove()


# Tab 3 voor commentaar zie Tab 4 onder aan de code
def add_marker_event3(coords):
    mapWidget3.delete_all_path()
    marker3.set_position(coords[0], coords[1])
    mapWidget3.set_path([brussel, coords])

progressLabel3 = Label(tab3,text = "Laden...")
progressLabelBar3 = Progressbar(tab3, orient= HORIZONTAL, length=600)
mapWidget3 = tkintermapview.TkinterMapView(tab3, height=400, width=600)
mapWidget3.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite
mapWidget3.set_zoom(0)
mapWidget3.add_right_click_menu_command(label="Markeer Locatie",command=add_marker_event3,pass_coords=True)
locatie3 = mapWidget3.set_marker(brussel[0], brussel[1], text="Ik")
marker3 = mapWidget3.set_marker(1000.0, 1000.0, text="Locatie")


mapWidget3.grid(row = 0, column = 0, pady = 2)
progressLabelBar3.grid(row = 2, column = 0)

#maakt een nieuwe defenitie aan die helemaal apart loopt van het script en zorgt ervoor dat we alle api's krijgen van de derde tab en de main loop blijft lopen. zoals de sattelieten
def apiThreadFunction3():
    response = requests.get("https://celestrak.org/NORAD/elements/supplemental/sup-gp.php?FILE=starlink&FORMAT=json")
    data = response.json()
    lengt = len(data)
    done = 0
    progressLabel3.grid(row = 1, column = 0, pady = 2)
    for item in data:
        name = item["OBJECT_NAME"]
        id = item["NORAD_CAT_ID"]
        response = requests.get(f"https://api.n2yo.com/rest/v1/satellite/positions/{id}/0.0/0.0/0/1&apiKey=DESUBF-GMFG7A-BS3C6F-4ZD5")
        satdata = response.json()
        lat = satdata["positions"][0]["satlatitude"]
        lon = satdata["positions"][0]["satlongitude"]
        done += 1
        mapWidget3.set_marker(lat, lon, text=name)
        print(f"[{done}/{lengt}] {name}: lat: {lat} lon: {lon}")
        progressLabel3.config(text = f"Laden: [{done}/{lengt}]")
        progressLabelBar3["value"] = (done/lengt)*100
    progressLabel3.config(text = f"Alles Is Geladen")
    progressLabelBar3.grid_remove()


# Tab 4

def add_marker_event4(coords):#maakt een definitie aan en verwijderd alle paden en  maakt een nieuwe aan
    mapWidget4.delete_all_path()
    marker4.set_position(coords[0], coords[1])
    mapWidget4.set_path([brussel, coords])
#laat een laad balk zien met tekst erboven.
progressLabel4 = Label(tab4,text = "Laden...")
progressLabelBar4 = Progressbar(tab4, orient= HORIZONTAL, length=600)
#krijgen de map van google api met een bepaalde hoogte en breedte en zet start zoom op 0
mapWidget4 = tkintermapview.TkinterMapView(tab4, height=400, width=600)
mapWidget4.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite
mapWidget4.set_zoom(0)
#zorgt dat als je op rechtermuis klikt dat he ene menu ziet en een marker kan plaatsen naar brussel
mapWidget4.add_right_click_menu_command(label="Markeer Locatie",command=add_marker_event4,pass_coords=True)
locatie4 = mapWidget4.set_marker(brussel[0], brussel[1], text="Ik")
marker4 = mapWidget4.set_marker(1000.0, 1000.0, text="Locatie")
#voegt alles toe aan de grid afhankelijk van de gegeven posities
mapWidget4.grid(row = 0, column = 0, pady = 2)
progressLabelBar4.grid(row = 2, column = 0)

#maakt een nieuwe defenitie aan die helemaal apart loopt van het script en zorgt ervoor dat we alle api's krijgen van de vierde tab en de main loop blijft lopen. zoals de sattelieten
def apiThreadFunction4(): # # definitie voor functie
    response = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=weather&FORMAT=json") # krijg de info en plaats in variabele
    data = response.json() # variabele is gelijk aan het starten van het json-bestand
    lengt = len(data) # de lengte van variabele 'data' is gelijk aan variabele 'lengt'
    done = 0 # variabele is gelijk aan nul
    progressLabel4.grid(row = 1, column = 0, pady = 2) # dit is de positie voor het laad bar
    for item in data: # voor item in data
        name = item["OBJECT_NAME"] # de namen van de objecten worden toegevoegd aan de variabele
        id = item["NORAD_CAT_ID"] # de id's van de objecten worden toegevoegd aan de variabele
        response = requests.get(f"https://api.n2yo.com/rest/v1/satellite/positions/{id}/0.0/0.0/0/1&apiKey=DESUBF-GMFG7A-BS3C6F-4ZD5") # krijg de info uit de api en plaats in variabele
        satdata = response.json() # de functie om het json bestand te openen plaats je in deze variabele
        lat = satdata["positions"][0]["satlatitude"] # plaats de positie van de lengte graad
        lon = satdata["positions"][0]["satlongitude"] # plaats de postie van de breedte graad
        done += 1 # tel variabele op met 1
        mapWidget4.set_marker(lat, lon, text=name)#zet een marker op plaats van de naam en de long en lat
        print(f"[{done}/{lengt}] {name}: lat: {lat} lon: {lon}") # print alle waardes van de variabelen
        progressLabel4.config(text = f"Laden: [{done}/{lengt}]")#laat de laad balk zien en hoever die staat
        progressLabelBar4["value"] = (done/lengt)*100 # formule voor de waarde van de laad bar
    progressLabel4.config(text = f"Alles Is Geladen")#laat zien dat alles is geladen
    progressLabelBar4.grid_remove() # verwijder de laad bar uit de grid 

#maakt alle threads aan en start alle bijhorende functies voor de gebruiker
apiThread1 = threading.Thread(target=apiThreadFunction1)
apiThread2 = threading.Thread(target=apiThreadFunction2)
apiThread3 = threading.Thread(target=apiThreadFunction3)
apiThread4 = threading.Thread(target=apiThreadFunction4)
apiThread1.start() 
apiThread2.start() 
apiThread3.start() 
apiThread4.start() 

#start de mainloop om het programma te laten lopen.
root.mainloop()