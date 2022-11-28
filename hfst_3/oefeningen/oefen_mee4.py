woord = input("Geef een woord op: ")
if len(woord) < 5:
    klein_woord = True

try:
    print(f"Huidige waarde klein_woord: {klein_woord}")
except NameError:
    # Je mag de code enkel hier aanpassen. 
    # Los het probleem van de exception op.
    pass

if klein_woord:
    print(f"{woord} is een klein woord")
else:
    print(f"{woord} is een groot woord")
