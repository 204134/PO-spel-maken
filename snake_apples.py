import pygame
from random import randint

class Apple():
    def __init__(self):
        self.apple_list = []
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("appel.png").convert_alpha()
        width = 30
        height = 30
        self.imageSmall = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen, game_over):
        if not game_over:
            if not self.apple_list:  # Als er geen appel is, genereer een nieuwe
                width = 30
                height = 30
                self.x = randint(0, 800 - width)
                self.y = randint(0, 600 - height)
                self.apple_list.append('apple')  # Voeg een appel toe aan de lijst

            # Teken de appel op het scherm
            screen.blit(self.imageSmall, (self.x, self.y))
