class Hond:
    def __init__(self, naam, massa):
        self.name = naam
        self.mass = massa

    def weegschaal(self):
        print(f"{self.name} weegt {self.mass} kilo")

hond = Hond("juul",3)
hond2 = Hond("adam", 5)
hond.weegschaal()
hond2.weegschaal()