class Kat:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def oud(self):
        print(f"{self.naam} is {self.leeftijd}")

kater = Kat("Marcel", 9)
kater.oud()

kitten = Kat("Fred", 1)
kitten.oud()
