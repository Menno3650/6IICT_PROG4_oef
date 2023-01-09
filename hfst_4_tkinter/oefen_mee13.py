# Importeer tkinter module. Geef naam tk.
# Importeer random module
import tkinter as tk, random

# Maak een lege GUI aan.
venster = tk.Tk()

random_getal = -1
def genereer():
    # Breng de variabele random_getal in de functie.
    global random_getal
    # Lees de waarde van entry_1 uit.
    tekst = entry_1.get()

    # Enkel als tekst een getal is, mag random.randint() uitgevoerd worden.
    if not tekst.isnumeric():
        resultaat = "Entry slecht ingevuld"
    else:
        random_getal = random.randint(0, int(tekst))
        resultaat = "Getal berekend"
    
    # Toon of functie geslaagd is.
    label = tk.Label(padx=40, pady=5, master=venster, text=resultaat)
    label.grid(row=3,column=0)

# TODO: bereken hoeveel de gok van de gebruiker langs random_getal zat.
def bereken_erlangs():
    pass


# Zet labels met uitleg klaar.
label = tk.Label(padx=40, pady=5, master=venster, text="Geef een getal in: ")
label.grid(row=0, column=0)
label = tk.Label(padx=40, pady=5, master=venster, text="Gok het gegenereerde getal: ")
label.grid(row=0,column=1)

# Zet invulvelden klaar.
entry_1 = tk.Entry() 
entry_1.grid(row=1, column=0)
entry_2 = tk.Entry()
entry_2.grid(row=1, column=1) 

# Zet knoppen klaar.
knop_1 = tk.Button(pady=10, master=venster, text="Genereer getal", command=genereer)
knop_1.grid(row=2, column=0)
knop_2 = tk.Button(pady=10, master=venster, text="Gok het getal", command=bereken_erlangs)
knop_2.grid(row=2, column=1)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()