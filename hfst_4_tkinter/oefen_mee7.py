import tkinter as tk

venster = tk.Tk()

label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2, 
                 highlightthickness=2, highlightbackground="black")
label.grid(row=0, column=0)

veld = tk.Entry(master=venster, width=50, fg="red")
veld.grid(row=0, column=1)

def display_naam():
    tekst = f"Hallo, mijn naam is {veld.get()}!"
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)
    label_naam.grid(row=2, column=0, columnspan=2)

knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50)
knop.grid(row=1, column=0, columnspan=2)

venster.mainloop()
