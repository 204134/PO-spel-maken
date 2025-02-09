   
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
    def __init__(self, position, x=0, y=0, direct='right', new=False):
        # Richting en positie van de slangsegmenten
        self.direction = direct  # Standaard naar rechts

        # Initialisatie van de afbeelding
        if position == 0:  # Hoofd
            self.image = pygame.image.load(settings.slangenhoofd).convert_alpha()
            self.imageSmall = pygame.transform.scale(self.image, (settings.snakeHead_width, settings.snakeHead_height))
        else:  # Lichaamsdelen
            self.image = pygame.image.load(settings.slangenlichaam).convert_alpha()
            self.imageSmall = pygame.transform.scale(self.image, (settings.snake_width, settings.snake_height))

        # Stel de beginpositie in (standaard beginpunt is (0, 0))
        if x == 0 and y == 0:
            self.x = settings.x - position * settings.snake_width
            self.y = settings.y

        # Als het een nieuw segment is
        if new:
            if direct == 'left':
                self.x = x + settings.snelheid
                self.y = y
            elif direct == 'right':
                self.x = x - settings.snelheid
                self.y = y
            elif direct == 'up':
                self.y = y + settings.snelheid
                self.x = x
            elif direct == 'down':
                self.y = y - settings.snelheid
                self.x = x

        self.position = position  # Het segmentnummer (hoofd of lichaam)
        
    def move(self, up, down, left, right, moves_list = []):
        #print(str(up) + str(down) +str(left)+str(right)+str(moves_list))
        if self.position == 0:
            if left:
                self.x -= settings.snelheid
                self.direction = 'left'
                moves_list.append('left')
            elif right:
                self.x += settings.snelheid
                self.direction = 'right'
                moves_list.append('right')
            elif up:
                self.y -= settings.snelheid
                self.direction = 'up'
                moves_list.append('up')
            elif down:
                self.y += settings.snelheid
                self.direction = 'down'
                moves_list.append('down')

            self.rotate_image()  # Roep de functie aan om de afbeelding te roteren

            return moves_list
        else:
            #print(moves_list)
            if moves_list:
                try:
                    direction = moves_list[-(self.position+1)]
                except IndexError:
                    try:
                        direction = moves_list[-self.position]
                    except IndexError:
                        try:
                            direction = moves_list[-self.position+1]
                        except IndexError:
                            direction = moves_list[-1]
                    
                #print ('check: '+str(self.x)+str(self.y)+str(direction))
                if direction == 'left':
                    self.x -= settings.snelheid
                elif direction == 'right':
                    self.x += settings.snelheid
                elif direction == 'up':
                    self.y -= settings.snelheid
                elif direction == 'down':
                    self.y += settings.snelheid
                if len(moves_list)>768:
                    moves_list.pop(0)
                return self.x, self.y, direction
            
    def check_pos(self):
        # Controleer of de slang buiten het scherm gaat
        if self.x >= 800 or self.x < 0 or self.y >= 600 or self.y < 0:
            game_over = True
        else:
            game_over = False
        return game_over

    def update(self, game_over, color=settings.green):
        # Teken de slang
        if not game_over:
            if self.position == 0:
                settings.screen.blit(self.imageRotated, (self.x, self.y))
            else:
                settings.screen.blit(self.imageSmall, (self.x, self.y))
            #pygame.draw.rect(settings.screen, color, (self.x, self.y, settings.snake_width, settings.snake_height))
        
    def collision(self, x, y):
        #print("colission checking")
        if self.x == x and self.y == y:
            print ("collided")
            return True
        return False
    
    def rotate_image(self):
        if self.position == 0:  # Alleen het hoofd moet roteren
            if self.direction == 'left':
                self.imageRotated = pygame.transform.rotate(self.imageSmall, 180)
            elif self.direction == 'right':
                self.imageRotated = self.imageSmall  # Originele afbeelding
            elif self.direction == 'up':
                self.imageRotated = pygame.transform.rotate(self.imageSmall, 90)
            elif self.direction == 'down':
                self.imageRotated = pygame.transform.rotate(self.imageSmall, -90)


