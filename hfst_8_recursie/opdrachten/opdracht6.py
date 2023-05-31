import pygame
 
# Colors
ZWART = (0, 0, 0)
WIT = (255, 255, 255)
 
""" Recursieve fractaal functie.
    Het tekenen van 'H' op het scherm gebeurt als volgt:
    teken_h(x, y, breedte, hoogte, scherm)
 """
def recursieve_fractaal(x, y, breedte, hoogte, diepte, scherm):
    # TODO: maak deze functie recursief.
    teken_h(x, y, breedte, hoogte, scherm) # Teken een H volgens de meegegeven dimensies.

 

 
""" Teken een H op een bepaalde positie (x,y) & een bepaalde grootte (breedte,hoogte). """
def teken_h(x,y,breedte,hoogte, scherm):
    pygame.draw.line(scherm,
                    ZWART,
                    [x + breedte*.25, hoogte // 2 + y],
                    [x + breedte*.75, hoogte // 2 + y],
                    3)
    pygame.draw.line(scherm,
                    ZWART,
                    [x + breedte * .25, (hoogte * .5) // 2 + y],
                    [x + breedte * .25,  (hoogte * 1.5) // 2 + y],
                    3)
    pygame.draw.line(scherm,
                    ZWART,
                    [x + breedte * .75, (hoogte * .5) // 2 + y],
                    [x + breedte * .75, (hoogte * 1.5) // 2 + y],
                    3)

""" Open pygame scherm met instellingen voor rechthoek.  """
def main(): 
    # Instellingen 
    running = True
    breedte, hoogte = 700, 700
    diepte = 3
    pygame.init()
    scherm = pygame.display.set_mode([breedte, hoogte])
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    
    # -------- Main Loop -----------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        scherm.fill(WIT)

        """ Teken fractalen zoals aangeven op GitHub. """
        recursieve_fractaal(0, 0, breedte, hoogte, diepte, scherm)
    
        pygame.display.flip()
        clock.tick(20)
    
    pygame.quit()

if __name__ == "__main__":
    main()