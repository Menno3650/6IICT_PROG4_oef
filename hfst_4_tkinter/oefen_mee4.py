# Importeer tkinter module. Geef naam tk.
import tkinter as tk
from tkinter import *
# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: maak het roosterpatroon van oefen mee 4. 
label_1 = tk.Label(master=venster, text="(0,0)")
label_2 = tk.Label(master=venster, text= "(0,1)")
label_3 = tk.Label(master=venster, text= "(0,2)")

label_4 = tk.Label(master=venster, text= "(1,0)")
label_5 = tk.Label(master=venster, text= "(1,1) - columnspan=2")

label_6 = tk.Label(master=venster, text= "(2,0)rowspan = 2")
label_7 = tk.Label(master=venster, text= "(2,1)")
label_8 = tk.Label(master=venster, text= "(3,1")
label_9 = tk.Label(master=venster, text= "(2,2)")
label_10 = tk.Label(master=venster, text= "(3,2)")
# Label toevoegen aan de master (in dit geval venster).
label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)

label_4.grid(row=1, column=0)
label_5.grid(row=1, column=1, columnspan=2)

label_6.grid(row=2, column=0, rowspan=2)
label_7.grid(row=2, column=1)
label_8.grid(row=3, column=1)
label_9.grid(row=2, column=2)
label_10.grid(row=3, column=2)


scrollbar = Scrollbar(venster)
# Maak de GUI zichtbaar op de computer.
venster.mainloop()
