class Bankrekening:
    bank = "KBC"

    def __init__(self, eigenaar, geld, leeftijd):
        self.eigenaar = eigenaar
        self.geld = geld
        self.leeftijd = leeftijd

    def storten(self, bedrag, bericht):
        self.geld += bedrag
        print(f"{bedrag} euro toegevoegd. Reden: {bericht}")

    def afhalen(self, bedrag, bericht):
        if self.leeftijd >= 16:
            if self.geld >= bedrag:
                self.geld -= bedrag
                print(f"{bedrag} euro afgehaald. Reden: {bericht}")
            else:
                print(f"Onvoldoende saldo om {bedrag} euro af te halen.")
        else:
            print(f"{self.eigenaar} is te jong om geld af te halen.")

    def overzicht(self):
        print(f"{self.eigenaar} heeft {self.geld} euro staan bij {self.bank}.")

    def overschrijven(self, bedrag, andere_rekening):
        if isinstance(andere_rekening, Bankrekening):
            if self.geld >= bedrag:
                self.geld -= bedrag
                andere_rekening.geld += bedrag
                print(f"{self.eigenaar} stort {bedrag} euro naar {andere_rekening.eigenaar}.")
            else:
                print(f"{self.eigenaar} heeft onvoldoende saldo om {bedrag} euro over te schrijven.")
        else:
            print("Geen geldige rekening meegegeven.")