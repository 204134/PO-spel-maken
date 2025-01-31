import pygame
from random import randint

class Apple():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("appel.png").convert_alpha()
        width = 30
        height = 30
        self.imageSmall = pygame.transform.scale(self.image, (width, height))
        self.new_position()
    
    def new_position(self):
        """Genereer een nieuwe willekeurige positie voor de appel."""
        self.x = randint(0, 800 - 30) // 25 * 25  #Zorgt dat het op een raster zit
        self.y = randint(0, 600 - 30) // 25 * 25

    def draw(self, screen, game_over):
        if not game_over:
            screen.blit(self.imageSmall, (self.x, self.y))
