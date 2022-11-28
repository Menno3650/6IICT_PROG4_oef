# Maak Conway's Game of Life na. https://www.youtube.com/watch?v=C2vgICfQawE
 
import copy,json,pygame,random


fp = open("oefening_za.json", "r")
settings = json.load(fp)
fp.close()

def maak_rij_nul(breedte):
    return [0]*breedte

def maak_veld_nul(hoogte, breedte):
    veld = []
    for _ in range(hoogte):
        veld.append(maak_rij_nul(breedte))
    return veld

def maak_veld_nul_levend(veld, kans_levend):
    for y, rij in enumerate(veld):
        for x, cel in enumerate(rij):
            if random.random() < kans_levend:
                veld[y][x] = 1            

def tel_buren(veld, y, x):
    teller = 0

    # Controleer alle cellen rondom huidige cel.
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if (j == 0) and (i == 0):
                continue # Sla de huidige cel over.
            teller += veld[y+j][x+i]

    return teller

def leeft_of_sterft(veld, y, x):
    if veld[y][x] == 1: # Cel leeft
        if (tel_buren(veld, y, x) == 2) or (tel_buren(veld, y, x) == 3):
            return True  # Cel blijft leven
        else:
            return False # Cel sterft
    else: # Cel is dood
        if (tel_buren(veld, y, x) == 3):
            return True  # Cel komt tot leven
        else:
            return False # Cel blijft dood

def update_veld(veld):
    """Update het veld volgens de regels van the game of life"""
    # Maak een kopie van het huidige veld
    huidig_veld = copy.deepcopy(veld)

    # Bepaal welke cel leeft/sterft. Update het veld op basis hiervan.s
    for y, rij in enumerate(huidig_veld):
        for x, _ in enumerate(rij):
            leeft = leeft_of_sterft(huidig_veld, y, x)
            if leeft:
                veld[y][x] = 1
            else:
                veld[y][x] = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings["BREEDTE"] * settings["CEL_HOOGTE"], settings["HOOGTE"] * settings["CEL_HOOGTE"]))
    clock = pygame.time.Clock()

    veld = maak_veld_nul(settings["HOOGTE"], settings["BREEDTE"])
    maak_veld_nul_levend(veld, settings["KANS_LEVEND"])

    running = True
    while running:
        # Maak scherm leeg. Update vervolgens OBV cel-waarde.
        screen.fill( settings["KLEUR_ACHTERGROND"] )
        for y, rij in enumerate(veld):
            for x, cel in enumerate(rij):
                if cel:
                    color = settings["KLEUR_LEVEND"]
                else:
                    color = settings["KLEUR_DOOD"]
                # Kleur viekant op scherm OBV kleur cel.
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x * settings["CEL_BREEDTE"],
                        y * settings["CEL_HOOGTE"],
                        settings["CEL_BREEDTE"],
                        settings["CEL_HOOGTE"],
                    ),
                )

        # Update all cellen in het veld.
        update_veld(veld)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(2)


if __name__ == "__main__":
    main()