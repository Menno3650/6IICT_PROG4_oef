import random

class Hond:
    locaties = ["living", "tuin", "buren"]
    def __init__(self, naam):
        self.naam = naam
        self.locatie = random.choice(self.locaties)

    def ziet_hond(self, andere_hond):
        if self.locatie == andere_hond.locatie:
            print(f"{self.naam} ziet {andere_hond.naam} in de {self.locatie}.")

            gekozen = random.choice([self,andere_hond])
            gekozen.locatie = random.choice(self.locaties)
            print(f"{gekozen.naam} is bang en rent naar de {self.locatie}.")
        else:
            print(f"{self.naam} ziet geen hond in de/het {self.locatie}.")

hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
hond_3 = Hond("Ranger")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)
hond_2.ziet_hond(hond_3)
