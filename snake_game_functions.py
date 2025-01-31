import pygame
from snake_settings import Settings

# Initialiseer pygame
pygame.init()

# Initialiseer onze eigen modules
ssettings = Settings()

gestart = False

class Game_functions():
    def __init__(self):
        # variabelen
        self.x = 300
        self.y = 250
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.start_right = False
        self.moves_list = []
        
    def check_keydown_events(self, game_over):
        global gestart
        #print("checking events..")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # Beweeg de slang alleen als het spel niet over is
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not (self.down or self.start_right) and gestart: #Gestart zorgt ervoor dat er niet kan worden begonnen met naar links te gaan
                    self.up = True
                    self.left = self.right = False
                elif event.key == pygame.K_DOWN and not (self.up or self.start_right) and gestart:
                    self.down = True
                    self.left = self.right = False
                elif event.key == pygame.K_LEFT and not (self.right or self.start_right) and gestart:
                    self.left = True
                    self.up = self.down = False
                elif event.key == pygame.K_RIGHT and not self.left:
                    self.right = True
                    self.up = self.down = False
                    self.start_right = False
                    gestart = True
                    
        return self.up, self.down, self.left, self.right
    
    def reset(self):
        global snake, snake_head, moves_list, game_over
        print("reset")
        # Reset de spelstatus
        self.x = 300
        self.y = 250
        self.left = self.right = self.up = self.down = False
        self.moves_list = []
        self.start_right = True
        
        snake = []
        snake_head = Snake_piece(0)  # Nieuw slanghoofd maken
        snake1 = Snake_piece(1)
        snake2 = Snake_piece(2)
        snake3 = Snake_piece(3)
        snake.append(snake1)
        snake.append(snake2)
        snake.append(snake3)

        # Reset de appel
        apple.new_position()  # Zorg dat de appel een nieuwe plek krijgt
        
