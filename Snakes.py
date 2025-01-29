import pygame
from snake_settings import Settings
from snake_game_functions import Game_functions
from snake import Snake_piece
from snake_buttons import Button
from snake_apples import Apple

# Initialiseer pygame
pygame.init()

# Initialiseer onze eigen modules
settings = Settings()
gf = Game_functions()
button = Button()
apple = Apple()

# Initialiseer lijsten
snake = []
moves_list = []
# het slangenhoofd
snake_head = Snake_piece(0, True)
# de eerste lichaamsdelen
snake1 = Snake_piece(1, True)
snake.append(snake1)
snake2 = Snake_piece(2, True)
snake.append(snake2)
snake3 = Snake_piece(3, True)
snake.append(snake3)

# enkele instellingen
pygame.display.set_caption("Snakes")
clock = pygame.time.Clock()

# Hoofdlus
running = True
game_over = False

while running:
    settings.screen.fill(settings.black)  #Vul de achtergrond met zwart
    up, down, left, right = gf.check_keydown_events(game_over)
    game_over = button.check_clicked(game_over)
    
    if not game_over:
        # Beweeg de slang, update & controleer locatie
        apple.draw(game_over)
        snake_head.update(game_over)
        moves_list = snake_head.move(up, down, left, right, moves_list)
        for snake_part in snake:
            snake_part.update(game_over)
            snake_part.move(up, down, left, right, moves_list)
        game_over = snake_head.check_pos()
        if snake_head.apple_collision():
            n = len(snake)
            snake_piece = Snake_piece(n, False)
            snake.append(snake_piece)
        
    else:
        # Teken het groene vierkant en de tekst
        gf.reset()
        game_over = False
        pygame.draw.rect(settings.screen, settings.green, settings.game_over_rect)
        settings.screen.blit(settings.lose_text, settings.lose_text_rect) 
        button.draw(200, 400, 400, 50, "Opnieuw starten", settings.red, settings.white)
       
    pygame.display.flip()  # Werk het scherm bij
    clock.tick(5)  # Beperk de framesnelheid tot 30 FPS

pygame.quit()
