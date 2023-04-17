import pygame
from particle import BoringParticle

# Constantes.
breedte, hoogte = 600,600
fps = 120
aantal_particles = 20

# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((breedte,hoogte))
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.
particles = []  
""" Vul lijst aan... """
    
running = True
while running:
    # Maak scherm schoon.
    scherm.fill((0,0,0))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(fps)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).
    for particle in particles:
        """ 1. Beweeg particle """
        """ 2. Reset particle """
        pygame.draw.circle(scherm, (255,255,255), ("3. Vul aan met x-/y-positie van particle"), 10)

    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()