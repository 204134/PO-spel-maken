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
snake_head = Snake_piece(0)
# de eerste lichaamsdelen
snake1 = Snake_piece(1)
snake.append(snake1)
snake2 = Snake_piece(2)
snake.append(snake2)
snake3 = Snake_piece(3)
snake.append(snake3)

#Enkele instellingen
pygame.display.set_caption("Snakes")

#Kleur en klok instellen
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
gray = (169, 169, 169)

clock = pygame.time.Clock()
speed=settings.spel_snelheid

# Hoofdlus
running = True
game_over = False

# maak de eerste appel
apple_x, apple_y = apple.new_pos()

while running:
    settings.screen.fill(settings.black)  #Vul de achtergrond met zwart
    up, down, left, right = gf.check_keydown_events(game_over)
    game_over = button.check_clicked(game_over)
    if not game_over:
        # Beweeg de slang, update & controleer locatie
        apple.draw(game_over, apple_x, apple_y)
        moves_list = snake_head.move(up, down, left, right, moves_list)
        snake_head.update(game_over)
        if up or down or left or right:
            for snake_part in snake:
                snake_x, snake_y,direction = snake_part.move(up, down, left, right, moves_list)
                snake_part.update(game_over)
                if snake_head.collision(snake_x, snake_y):
                    game_over = True
           
        else:
            for snake_part in snake:
                snake_part.move(up, down, left, right, moves_list)
                snake_part.update(game_over)
        if snake_head.check_pos():
            game_over = True
        
        #if up or down or left or right: (kijk wat er gebeurt als je 'if snake_head.collision(apple_x, apple_y):' hiervoor vervangt. Het is erg leuk.
        if snake_head.collision(apple_x, apple_y):
            apple_x, apple_y = apple.new_pos()
            n = len(snake)+1
            snake_piece = Snake_piece(n, snake_x, snake_y, direction, True)
            snake_piece.update(game_over, settings.green)
            snake.append(snake_piece)
            #print(snake)
            speed += settings.snelheid_verhoging
    else:
        #game over text
        game_over_rect = pygame.Rect(150, 200, 500, 150)
        pygame.draw.rect(screen, gray, game_over_rect)
        pygame.draw.rect(screen, red, game_over_rect, 5)
        lose_text = font.render("Jij hebt dit spel verloren", True, white)
        lose_text_rect = lose_text.get_rect(center=game_over_rect.center)
        screen.blit(lose_text, lose_text_rect)
        # Teken het groene vierkant en de tekst
        #print(game_over)
        pygame.draw.rect(settings.screen, settings.green, settings.game_over_rect)
        settings.screen.blit(settings.lose_text, settings.lose_text_rect) 
        button.draw(200, 400, 400, 50, "Opnieuw starten", settings.red, settings.white)
        print('reset')
        gf.reset()
        game_over = False

        
       
    pygame.display.flip()  # Werk het scherm bij
    clock.tick(speed)  # Beperk de framesnelheid tot 30 FPS
    

pygame.quit()
