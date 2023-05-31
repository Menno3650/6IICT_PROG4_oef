import pygame
import random

# Constants
SCREEN_WIDTH = 534
SCREEN_HEIGHT = 600
FPS = 60
PLAYER_SIZE = 50
PLAYER_SPEED = 5
CAR_WIDTH = 50
CAR_HEIGHT = 100
CAR_SPEED = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

class Car(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), y)

    def update(self):
        self.rect.y += CAR_SPEED
        if self.rect.top > SCREEN_WIDTH:
            self.rect.bottom= 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

imp = pygame.image.load(r"C:\Users\Menno\OneDrive\Documenten\GitHub\6IICT_PROG4_oef\hfst_6_oop\oefenmee\road.png").convert()
 
# Using blit to copy content from one surface to other


for i in range(5):
    car = Car(random.randint(0, SCREEN_HEIGHT - CAR_HEIGHT))
    all_sprites.add(car)
    cars.add(car)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Check collision between player and cars
    if pygame.sprite.spritecollide(player, cars, False):
        running = False

    screen.blit(imp, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
