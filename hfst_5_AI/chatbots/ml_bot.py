from Levenshtein import distance


class ML_Chatbot:
    conversatie = {}

    def __init__(self, name):
        self.name = name

    def train(self, conversatie):
        self.conversatie = conversatie

    def zoek_antwoord(self, vraag):
        if self.conversatie == {}:
            return "Geen antwoord"

        vraag = vraag.lower()

        laagste_afstnad = 99999
        beste_antwoord = "Geen antwoord"

        for gekende_vraag, antwoord in self.conversatie.items():
            huidige_afstand = distance(vraag, gekende_vraag.lower())
            huidige_afstand = huidige_afstand / max(len(gekende_vraag), len(vraag))
            if huidige_afstand < laagste_afstnad:
                laagste_afstnad = huidige_afstand
                beste_antwoord = antwoord

        return beste_antwoord

    def vraag_reeks(self):
        print("Zeg 'stop' om de conversatie te stoppen.")

        while True:
            user_input = input()
            if user_input == "stop":
                break

            bot_response = self.zoek_antwoord(user_input)
            print(bot_response)


bot = ML_Chatbot("Marvin")
print(bot.zoek_antwoord("Test"))
