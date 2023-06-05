import os

""" Niveau 1: zoek aantal bestanden in een hoofdmap. """

# Cijfers geven aantal bestanden aan. Mappen zijn niet meegeteld.
print( doorzoek_map("hfst_4_tkinter") )     # 40 
print( doorzoek_map("hfst_7_hacken") )      # 553 
print( doorzoek_map("hfst_8_recursie") )    # 18 


""" Niveau 2 """

# Cijfers zijn in MB.
print( grootte_map("hfst_4_tkinter") )     # 0.09989 
print( grootte_map("hfst_7_hacken") )      # 190.92 
print( grootte_map("hfst_8_recursie") )    # 0.006324 