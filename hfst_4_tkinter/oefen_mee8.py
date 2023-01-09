import tkinter as tk

venster = tk.Tk()

label = tk.Label(master=venster, text="Welke website wil je bezoeken?", height=2)
label.grid(row=0, column=0, columnspan=2)

link_1 = tk.Entry(master=venster, width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
link_1.grid(row=1, column=0)

link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14), 
                  border=10, borderwidth=5)
link_2.grid(row=1, column=1)

def reset_links():
    link_1.delete(0, 1)

    web_2 = link_2.get()
    link_2.delete( 0, web_2.find(".")+1 )

knop = tk.Button(master=venster, command=reset_links, 
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)

venster.mainloop()