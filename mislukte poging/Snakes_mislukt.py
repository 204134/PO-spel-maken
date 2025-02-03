import pygame
from ss_mislukt import Settings
from sgf_mislukt import Game_functions
from s_mislukt import Snake_piece
from sb_mislukt import Button

# Initialiseer pygame
pygame.init()

# Initialiseer onze eigen modules
settings = Settings()
gf = Game_functions()
button = Button()

# Maak de slang
snake = []
# het slangenhoofd
snake_head = Snake_piece(0)
snake.append(snake_head)
# de eerste lichaamsdelen
snake1 = Snake_piece(1)
snake.append(snake1)
snake2 = Snake_piece(2)
snake.append(snake2)
snake3 = Snake_piece(3)
snake.append(snake3)

# enkele instellingen
pygame.display.set_caption("Snakes")
clock = pygame.time.Clock()

# Hoofdlus
running = True
game_over = False

while running:
    settings.screen.fill(settings.black)  #Vul de achtergrond met zwart
    moves_list = gf.check_keydown_events(game_over)
    game_over = button.check_clicked(game_over)
    
    if not game_over:
        # Beweeg de slang, update & controleer locatie
        
        for snake_part in snake:
            snake_part.move(moves_list)
            snake_part.update(game_over)
            
        game_over = snake_head.check_pos()
        
    else:
        # Teken het groene vierkant en de tekst
        pygame.draw.rect(settings.screen, settings.green, settings.game_over_rect)
        settings.screen.blit(settings.lose_text, settings.lose_text_rect) 
        button.draw(200, 400, 400, 50, "Opnieuw starten", settings.red, settings.white)
       
    pygame.display.flip()  # Werk het scherm bij
    #clock.tick(5)  # Beperk de framesnelheid tot 30 FPS

pygame.quit()
