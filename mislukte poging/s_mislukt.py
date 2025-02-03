import pygame
from ss_mislukt import Settings
from sgf_mislukt import Game_functions

# Initialiseer pygame
pygame.init()

# initialiseer de modules
settings = Settings()
gf = Game_functions()

class Snake_piece():
    def __init__(self, position):
        # Slang variabele
        self.x = (gf.x - position*settings.snake_width)
        self.y = gf.y
        self.position = position
        
    def move(self, moves_list = gf.moves_list):
        #print("Hello")
        if moves_list:
            try:
                direction = moves_list[-(1+self.position)]
            except IndexError:
                try:
                    direction = moves_list[-self.position]
                except IndexError:
                    try:
                        direction = moves_list[-self.position+1]
                    except IndexError:
                        direction = moves_list[-1]
                        
            print(direction)
            if direction == 'left':
                self.x -= settings.snelheid
                print('1')
            if direction == 'right':
                self.x += settings.snelheid
                print('2')
            if direction == 'up':
                self.y -= settings.snelheid
                print('3')
            if direction == 'down':
                self.y += settings.snelheid
                print('4')
            
    def check_pos(self):
        # Controleer of de slang buiten het scherm gaat
        if self.x >= 800 or self.x < 0 or self.y >= 600 or self.y < 0:
            game_over = True
        else:
            game_over = False
        return game_over

    def update(self, game_over):
        # Teken de slang
        if not game_over:
            pygame.draw.rect(settings.screen, settings.green, (self.x, self.y, settings.snake_width, settings.snake_height))
