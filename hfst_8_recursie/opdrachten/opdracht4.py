import pygame
 
# Kleuren
ZWART = (0, 0, 0)
WIT = (255, 255, 255)

""" 
Recursieve rechthoek functie.
Het tekenen van rechthoeken op het scherm kan als volgt: 
pygame.draw.rect(scherm, ZWART, [x, y, breedte, hoogte], 1)
"""
def recursieve_rechthoek(x, y, breedte, hoogte, scherm):
    # TODO: maak deze functie recursief.
    pygame.draw.rect(scherm, ZWART,[x, y, breedte, hoogte], 1) # Teken een rechthoek volgens de meegegeven dimensies.


""" Open pygame scherm met instellingen voor rechthoek. """
def main(): 
    # Instellingen 
    running = True
    breedte, hoogte = 700, 500
    pygame.init()
    scherm = pygame.display.set_mode([breedte, hoogte])
    pygame.display.set_caption("Recursieve rechthoek")
    clock = pygame.time.Clock()
    
    # -------- Main Loop -----------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        scherm.fill(WIT)
    
        """ Teken rechthoeken zoals aangegeven op GitHub. """
        recursieve_rechthoek(0, 0, breedte, hoogte, scherm)
    
        pygame.display.flip()
        clock.tick(60)
    
    # Stop pygame
    pygame.quit()

if __name__ == "__main__":
    main()