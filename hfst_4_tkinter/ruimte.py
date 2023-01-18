import tkinter as tk

root = tk.Tk()

lb_frame = tk.Frame(root, bd=1, relief="sunken")
listbox = tk.Listbox(lb_frame, bd=0, yscrollcommand=lambda *args: vsb.set(*args))
vsb = tk.Scrollbar(lb_frame, orient="vertical", command=listbox.yview)

vsb.pack(side="right", fill="y")
listbox.pack(side="left", fill="both", expand=True)

lb_frame.pack(padx=20, pady=20)

for i in range(1, 100):
    listbox.insert("end", f"Item {i}")

root.mainloop()