class Hond:
    def __init__(self, naam, massa):
        self.name = naam
        self.mass = massa

    def weegschaal(self):
        print(f"{self.name} weegt {self.mass} kilo")


    def wijzig(self, naam):
        print(f"{self.name} heet nu {naam} ")
        self.name = naam 

    def eten(self,weeg):
        for i in range(3):
            self.mass += weeg*(1/3)
            print(f"{self.name} weegt nu {self.mass} kilo")
        
hond = Hond("juul",5)
hond.weegschaal()
hond.wijzig("aap")
hond.eten(0.5)

