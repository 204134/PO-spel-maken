import pygame
from random import randrange
from snake_settings import Settings

pygame.init()
settings = Settings()

class Apple():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("appel.png").convert_alpha()
        self.imageSmall = pygame.transform.scale(self.image, (settings.apple_width, settings.apple_height))
        self.apple_list = []
    
    def draw(self, screen, game_over):
        if not game_over:
            if not self.apple_list:  #Als er geen appel is, genereer een nieuwe
                # bepaal de willekeurige waarden van x en y, randrange ipv randint zorgt ervoor dat ook een stapsgrootte aangegeven kan worden.
                self.x = randrange(0, 800 - settings.apple_width, 25)
                self.y = randrange(0, 600 - settings.apple_height, 25)
                print('coords' + str(self.x) + ',' + str(self.y))
                self.apple_list.append('apple')  # Voeg een appel toe aan de lijst

            # Teken de appel op het scherm
            screen.blit(self.imageSmall, (self.x, self.y))