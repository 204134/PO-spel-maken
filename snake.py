import pygame
from snake_settings import Settings
from snake_game_functions import Game_functions
from snake_apples import Apple

# Initialiseer pygame
pygame.init()

# initialiseer de modules
settings = Settings()
apple = Apple()
gf = Game_functions()
 
class Snake_piece():
    def __init__(self, position, start_right):
        # Slang variabele
        self.x = (gf.x - (position)*settings.snake_width)
        self.y = gf.y
        self.position = position
        self.moves_list=[]
        self.start_right = start_right
        
    def move(self, up, down, left, right, moves_list = []):
        print (self.start_right)
        if self.position == 0:
            if left:
                self.x -= settings.snelheid
                moves_list.append('left')
            elif right or (right and self.start_right):
                self.x += settings.snelheid
                if not self.start_right:
                    moves_list.append('right')
                self.start_right = False
            elif up or (up and self.start_right):
                if self.start_right:
                    self.x += settings.snelheid
                self.y -= settings.snelheid
                moves_list.append('up')
                self.start_right = False
            elif down or (down and self.start_right):
                if self.start_right:
                    self.y -= settings.snelheid
                self.y += settings.snelheid
                moves_list.append('down')
                self.start_right = False
            return moves_list
        else:
            #print(moves_list)
            if self.start_right and (right or down or up):
                    self.x += settings.snelheid
                    self.start_right = False
            if moves_list:
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
        
    '''  
    def reset(self):
        self.start_right = True
    '''
