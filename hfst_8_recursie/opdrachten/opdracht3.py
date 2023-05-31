""" Niveau 1: zoek aantal bestanden in een hoofdmap. """

# Cijfers geven aantal bestanden aan. Mappen zijn niet meegeteld.
print( doorzoek_map("hfst_4_tkinter") )     # 40 
print( doorzoek_map("hfst_7_hacken") )      # 553 
print( doorzoek_map("hfst_8_recursie") )    # 18 


""" Niveau 2 """
def grootte_map(pad):
    items = os.listdir(pad)  # Zet de inhoud van de map in een lijst.
    grootte = 0

    for item in items: # Overloop ieder item.
        item_pad = os.path.join(pad, item)  # Haal pad van item op.

        if os.path.isfile(item_pad):        # Is item een bestand?
            grootte += os.path.getsize(item_pad) / (1024**2) 
        elif os.path.isdir(item_pad):       # Is item een map?
            grootte += grootte_map(item_pad)

    return grootte

# Cijfers zijn in MB.
print( grootte_map("hfst_4_tkinter") )     # 0.09989 
print( grootte_map("hfst_7_hacken") )      # 190.92 
print( grootte_map("hfst_8_recursie") )    # 0.006324 