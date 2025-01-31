import pygame
from snake_settings import Settings
from snake_game_functions import Game_functions

# Initialiseer pygame
pygame.init()

# initialiseer de modules
settings = Settings()
gf = Game_functions()

class Button():
    def __init__(self):
        pass

    def draw(self, x, y, w, h, text, color, text_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            pygame.draw.rect(settings.screen, color, (x, y, w, h))
            if click[0] == 1:
                return True  # Knop is geklikt
        else:
            pygame.draw.rect(settings.screen, color, (x, y, w, h), 2)

        text_surface = settings.font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
        settings.screen.blit(text_surface, text_rect)
        return False  # Knop is niet geklikt

    
    def check_clicked(self, game_over):
        #print("checking button..")
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        button_rect = pygame.Rect(200, 400, 400, 50)
                        if button_rect.collidepoint(event.pos):
                            gf.reset()
                            game_over = False
        return game_over
