class Hond:
    def __init__(self, naam, massa):
        self.name = naam
        self.mass = massa

    def weegschaal(self):
        print(f"{self.name} weegt {self.mass}")

hond = Hond()
hond.weegschaal()
