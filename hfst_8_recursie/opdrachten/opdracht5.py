
""" Bereken recursief de som van alle cijfers in een getal. """

print( optellen(12345) )            # 15
print( optellen(5) )                # 5
print( optellen(4687612962034330) ) # 65
print( optellen(6728003096702784) ) # 69

"""  Bepaal of het getal voldoet aan het Luhn algoritme. """
    
print( luhn(4687612962034330) ) # 70 --> geldig
print( luhn(6728003096702784) ) # 70 --> geldig
print( luhn(2727903413621029) ) # 66 --> ongeldig
print( luhn(9727009535679498) ) # 92 --> ongeldig