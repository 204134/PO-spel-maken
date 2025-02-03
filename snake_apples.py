import pygame
from random import randrange
from snake_settings import Settings

pygame.init()
settings = Settings()

class Apple():
    def __init__(self):
        self.image = pygame.image.load(settings.appel).convert_alpha()
        self.imageSmall = pygame.transform.scale(self.image, (settings.apple_width, settings.apple_height))
        self.apple_list = []
        self.x = 0
        self.y = 0
    
    def draw(self, game_over, x, y):
        if not game_over:
            # Teken de appel op het scherm
            settings.screen.blit(self.imageSmall, (x, y))
    
    def new_pos(self):
        #if not apple_list:#Als er geen appel is, genereer een nieuwe
            # bepaal de willekeurige waarden van x en y, randrange ipv randint zorgt ervoor dat ook een stapsgrootte aangegeven kan worden.
            #self.apple_list = apple_list
        self.x = randrange(0, 800 - settings.apple_width, 25)
        self.y = randrange(0, 600 - settings.apple_height, 25)
            #self.apple_list.append('apple')  # Voeg een appel toe aan de lijst
        return self.x,self.y
    
