       
import pygame
from snake_settings import Settings
from snake_apples import Apple

# Initialiseer pygame
pygame.init()

# Initialiseer onze eigen modules
settings = Settings()

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
    
    def reset(self, apple):
        from snake import Snake_piece
        global snake, game_over, apple_x, apple_y, moves_list, speed, direction

        print("Reset het spel...")

        # Zet de slang op de beginpositie
        start_x = 250  # Start x-coördinaat (midden van het scherm)
        start_y = 250  # Start y-coördinaat (midden van het scherm)
        snake_length = 4  # Aantal segmenten in de slang

        # Reset de slang naar een veilige positie (midden van het scherm)
        snake = []
        for i in range(snake_length):
            x_pos = start_x - i * settings.snake_width  # Plaats elk segment op de juiste plaats
            y_pos = start_y
            snake_piece = Snake_piece(i, x=x_pos, y=y_pos)
            snake.append(snake_piece)

        # Reset de bewegingenlijst
        moves_list = []  # Verwijder oude bewegingen

        # Reset de snelheid van het spel
        speed = settings.spel_snelheid

        # Reset de appel naar een nieuwe positie
        apple_x, apple_y = apple.new_pos()

        # Zet de game-over status opnieuw
        game_over = False

        # Reset de richting van de slang
        direction = "right"  # Start richting is naar rechts

        print("Spel is gereset!")

