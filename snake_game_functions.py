import pygame
from snake_settings import Settings

# Initialiseer pygame
pygame.init()

# Initialiseer onze eigen modules
settings = Settings()

class Game_functions():
    def __init__(self):
        # variabelen
        self.x = 300
        self.y = 250
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        
    def check_keydown_events(self, game_over):
        #print("checking events..")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # Beweeg de slang alleen als het spel niet over is
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not self.down:
                    self.up = True
                    self.left = self.right = False
                elif event.key == pygame.K_DOWN and not self.up:
                    self.down = True
                    self.left = self.right = False
                elif event.key == pygame.K_LEFT and not self.right:
                    self.left = True
                    self.up = self.down = False
                elif event.key == pygame.K_RIGHT and not self.left:
                    self.right = True
                    self.up = self.down = False
                    
        return self.up, self.down, self.left, self.right
    
    def reset(self):
        print("reset")
        # Reset de spelstatus
        self.x = 300
        self.y = 250
        self.left = self.right = self.up = self.down = False
        self.moves_list.clear()
        
