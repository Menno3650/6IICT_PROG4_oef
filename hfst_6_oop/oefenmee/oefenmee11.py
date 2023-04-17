class Hond:
    def __init__(self, naam):
        self.naam = naam
        self.eigenaar = ""

    def is_hond(self, eigenaar):
        if self.eigenaar == eigenaar.naam: ## of self.naam in hond.eigenaar
            return True
        else:
            return False

class Persoon:
    def __init__(self, naam):
        self.naam = naam
        self.honden = []

    def koop_hond(self, hond):
        if hond.eigenaar != "":
            print(f"{hond.naam} heeft reeds {hond.eigenaar} als eigenaar.")
            return 
        
        self.honden.append(hond)
        hond.eigenaar = self.naam

    def is_eigenaar(self, hond):
        if self.naam == hond.eigenaar:
            return True
        else:
            return False
        
hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
persoon_1 = Persoon("Jos")
persoon_2 = Persoon("Jef")

persoon_1.koop_hond(hond_1)
persoon_2.koop_hond(hond_2)
persoon_2.koop_hond(hond_1) # Lulu heeft reeds Jos als eigenaar.

print(persoon_1.is_eigenaar(hond_1)) # True
print(persoon_2.is_eigenaar(hond_1)) # False