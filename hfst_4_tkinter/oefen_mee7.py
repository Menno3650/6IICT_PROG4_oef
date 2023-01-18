import tkinter as tk#voegt module tkinter toe

venster = tk.Tk()#maakt venster aan

label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2, 
                 highlightthickness=2, highlightbackground="black")#maakt label aan en zet dit in grid
label.grid(row=0, column=0)

veld = tk.Entry(master=venster, width=50, fg="red")#maak een veld aan en voegt toe aan grid
veld.grid(row=0, column=1)

#functie om naam te lezen en te plaatsen in grid
def display_naam():
    tekst = f"Hallo, mijn naam is {veld.get()}!"
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)
    label_naam.grid(row=2, column=0, columnspan=2)
#maakt een knop en zet in grid
knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50)
knop.grid(row=1, column=0, columnspan=2)
# vensterr blijft in loop
venster.mainloop()
