class Hond:
    def weeg(self, massa):
        self.mass = massa
    def benoem(self, naam):
        self.name = naam

    def weegschaal(self):
        print(f"{self.name} weegt {self.mass} kilo")

hond = Hond()
hond.benoem("kip")
hond.weeg(5)
hond.weegschaal()

