# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

woord = ""


veld = tk.Entry(master=venster, font=("Helvetica",14), border=10, borderwidth=5)
veld.grid(row=0, column=0)

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is toevoegen van Entry veld aan Label onder de knop.

knop = tk.Button(master=venster, command=, text="Voeg toe aan string:", width=50)
knop.grid(row=1, column=0, pady=10, padx= 10)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()