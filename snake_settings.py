import pygame

# Initialiseer pygame
pygame.init()

class Settings():
    def __init__(self):
        
        # Scherm instellen
        self.screen = pygame.display.set_mode((800, 600))

        # Start settings
        self.x = 300
        self.y = 250

        # Spel settings
        self.spel_snelheid = 5
        self.snelheid_verhoging = 0.3 # hoeveel sneller de slang wordt na een appel gegeten te hebben

        # Kleur en klok instellen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.font = pygame.font.Font(None, 50)
        
        # Slang settings
        self.snelheid = 25
        self.snakeHead_width = 35
        self.snakeHead_height = 25
        self.snake_width = 25
        self.snake_height = 25
        
        # Appel settings
        self.apple_width = 25
        self.apple_height = 25
        
        # Text settings
        self.game_over_rect = pygame.Rect(150, 200, 500, 150)
        self.lose_text = self.font.render("Jij hebt dit spel verloren", True, self.white)
        self.lose_text_rect = self.lose_text.get_rect(center=self.game_over_rect.center)
        
        # Gebruikte afbeeldingen:
        self.appel = 'appel_transparant.png' #ChatGPT is gebruikt om van de zwarte achtergrond een transparante achtergrond te maken
        self.slangenhoofd = 'snake-head-transparant.png'
        self.slangenlichaam = 'groen-slanglichaam.png'
