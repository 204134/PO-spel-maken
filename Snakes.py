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
    settings.screen.fill(settings.black)  # Vul de achtergrond met zwart

    # Teken het speelveld
    for row in range(24):  
        for col in range(32):  
            if (row + col) % 2 == 0:
                color = 'light gray'
            else:
                color = 'dark gray'
            pygame.draw.rect(settings.screen, color, [col * 25, row * 25, 25, 25])

    # Check voor toetsinvoer (beweging)
    up, down, left, right = gf.check_keydown_events(game_over)

    # Check voor knopdruk (opnieuw spelen)
    game_over = button.check_clicked(game_over)

    if not game_over:
        # Beweeg de slang en update locatie
        apple.draw(game_over, apple_x, apple_y)
        moves_list = snake_head.move(up, down, left, right, moves_list)
        snake_head.update(game_over)

        if up or down or left or right:
            for snake_part in snake:
                snake_x, snake_y, direction = snake_part.move(up, down, left, right, moves_list)
                snake_part.update(game_over)
                if snake_head.collision(snake_x, snake_y):
                    game_over = True
        else:
            for snake_part in snake:
                snake_part.move(up, down, left, right, moves_list)
                snake_part.update(game_over)

        if snake_head.check_pos():  # Check of de slang uit de grenzen gaat
            game_over = True

        # Check of de slang de appel eet
        if snake_head.collision(apple_x, apple_y):
            apple_x, apple_y = apple.new_pos()
            n = len(snake) + 1
            snake_piece = Snake_piece(n, snake_x, snake_y, direction, True)
            snake_piece.update(game_over, settings.green)
            snake.append(snake_piece)
            speed += settings.snelheid_verhoging  # Verhoog de snelheid na het eten van een appel
    else:
        # Game-over scherm
        game_over_rect = pygame.Rect(200, 150, 400, 300)
        pygame.draw.rect(settings.screen, settings.black, game_over_rect)
        pygame.draw.rect(settings.screen, settings.green, game_over_rect, 5)

        # Tekst weergeven
        lose_text = settings.font.render("Je hebt verloren!", True, settings.white)
        lose_text_rect = lose_text.get_rect(center=(400, 250))
        settings.screen.blit(lose_text, lose_text_rect)

        # Teken de knop "Opnieuw spelen"
        if button.draw(250, 300, 300, 50, "Opnieuw spelen", settings.red, settings.white):
            gf.reset(apple)  # Reset het spel en de slang
            game_over = False  # Zet game_over naar False zodat het spel doorgaat

    pygame.display.flip()  # Werk het scherm bij
    clock.tick(speed)  # Beperk de framesnelheid tot de ingestelde snelheid

pygame.quit()
