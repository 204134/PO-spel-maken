import pygame
from snake_settings import Settings
from snake_game_functions import Game_functions
from snake_apples import Apple

# Initialiseer pygame
pygame.init()

# initialiseer de modules
settings = Settings()
gf = Game_functions()
apple = Apple()

class Snake_piece():
    def __init__(self, position):
        # Slang variabele
        self.x = (gf.x - position*settings.snake_width)
        self.y = gf.y
        self.position = position
        self.moves_list=[]
        
    def move(self, up, down, left, right, moves_list = []):
        if self.position == 0:
            if left:
                self.x -= settings.snelheid
                #print('1')
                moves_list.append('left')
            elif right:
                self.x += settings.snelheid
                #print('2')
                moves_list.append('right')
            elif up:
                self.y -= settings.snelheid
                #print('3')
                moves_list.append('up')
            elif down:
                self.y += settings.snelheid
                #print('4')
                moves_list.append('down')
            return moves_list
        else:
            #print(moves_list)
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
                if direction == 'left':
                    self.x -= settings.snelheid
                elif direction == 'right':
                    self.x += settings.snelheid
                elif direction == 'up':
                    self.y -= settings.snelheid
                elif direction == 'down':
                    self.y += settings.snelheid  
            
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
    
    def apple_collision(self):
        if self.x == apple.x and self.y == apple.y:
            return True
        else:
            return False
