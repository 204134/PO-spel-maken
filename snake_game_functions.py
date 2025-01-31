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
        self.start_right = True
        
    def check_keydown_events(self, game_over):
        #print("checking events..")
        events = pygame.event.get()
        if events:
            event = events[0]
            if event.type == pygame.QUIT:
                running = False
                
            # Beweeg de slang alleen als het spel niet over is
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not (self.down or self.start_right): #Gestart zorgt ervoor dat er niet kan worden begonnen met naar links te gaan
                    self.up = True
                    self.left = self.right = False
                elif event.key == pygame.K_DOWN and not (self.up or self.start_right):
                    self.down = True
                    self.left = self.right = False
                elif event.key == pygame.K_LEFT and not (self.right or self.start_right):
                    self.left = True
                    self.up = self.down = False
                elif event.key == pygame.K_RIGHT and not self.left:
                    self.right = True
                    self.up = self.down = False
                    self.start_right = False
                    
        return self.up, self.down, self.left, self.right
    
    def reset(self):
        print("reset")
        # Reset de spelstatus
        self.x = 300
        self.y = 250
        self.left = self.right = self.up = self.down = False
        self.moves_list.clear()
        self.start_right = True
        
