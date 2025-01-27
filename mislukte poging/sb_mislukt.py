import pygame
from ss_mislukt import Settings
from sgf_mislukt import Game_functions

# Initialiseer pygame
pygame.init()

# initialiseer de modules
settings = Settings()
gf = Game_functions()

class Button():
    def __init__(self):
        pass

    def draw(self, x, y, w, h, text, color, text_color):
        #Tekent een knop en retourneert True als erop geklikt is.
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Controleer of de muis binnen de knop is
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            pygame.draw.rect(settings.screen, color, (x, y, w, h))
            if click[0] == 1:  # Linkermuisknop ingedrukt
                return True
        else:
            pygame.draw.rect(settings.screen, color, (x, y, w, h), 2)

        # Voeg tekst toe aan de knop
        text_surface = settings.font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
        settings.screen.blit(text_surface, text_rect)
    
    def check_clicked(self, game_over):
        #print("checking button..")
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if text_rect.collidepoint(event.pos):
                            gf.reset()
                            game_over = False
        return game_over
