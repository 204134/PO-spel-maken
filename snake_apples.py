import pygame
from snake_settings import Settings
from snake_game_functions import Game_functions
from random import randint

# Initialiseer pygame
pygame.init()

# initialiseer de modules
settings = Settings()
gf = Game_functions()

class Apple():
    def __init__(self):
        self.apple_list = []
        self.x = 0
        self.y = 0
    
    def draw(self, game_over):
        # Teken de slang
        if not game_over:
            if not self.apple_list:
                self.x = randint(0,800-settings.apple_width)
                self.y = randint(0,600-settings.apple_height)
            pygame.draw.rect(settings.screen, settings.red, (self.x,self.y, settings.apple_width, settings.apple_height))
            self.apple_list.append('apple')


    