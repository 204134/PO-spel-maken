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

#appel/score teller
appel_score = 0

#Kleur en klok instellen
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
gray = (169, 169, 169)

clock = pygame.time.Clock()
speed=settings.spel_snelheid

food_sfx = pygame.mixer.Sound('food.mp3') # Deze muziek komt van de github van nilchakraborty: 'https://github.com/nilchakraborty/Snake-Game/blob/main/music/music.mp3'
gameover_sfx = pygame.mixer.Sound('gameover.mp3')
music_sfx = pygame.mixer.Sound('music.mp3')
music_sfx.set_volume(0.4) #Geluid van de muziek aanpassen, anders kun je het food geluid niet meer horen.
music_sfx.play()

# Hoofdlus
running = True
game_over = False

# maak de eerste appel
apple_x, apple_y = apple.new_pos()

while running:
    pygame.display.set_caption('Aantal appels: ' + str(appel_score))

    # Teken het speelveld
    for row in range(24):  
        for col in range(32):  
            if (row + col) % 2 == 0:
                color = (222,236,237,255)
            else:
                color = (209,228,230,255)
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
                    gameover_sfx.play()
                    music_sfx.stop()
        else:
            for snake_part in snake:
                snake_part.move(up, down, left, right, moves_list)
                snake_part.update(game_over)

        if snake_head.check_pos():  # Check of de slang uit de grenzen gaat
            game_over = True
            gameover_sfx.play()
            music_sfx.stop() #Muziek stop met spelen, want je bent dood

        # Check of de slang de appel eet
        if snake_head.collision(apple_x, apple_y):
            apple_x, apple_y = apple.new_pos()
            n = len(snake) + 1
            snake_piece = Snake_piece(n, snake_x, snake_y, direction, True)
            snake_piece.update(game_over, settings.green)
            snake.append(snake_piece)
            speed += settings.snelheid_verhoging  # Verhoog de snelheid na het eten van een appel
            food_sfx.play()
            appel_score += 1
    else:
        # Game-over scherm
        game_over_rect = pygame.Rect(200, 150, 400, 300)
        #pygame.SRCALPHA betekent dat elke pixel van de surface een individuele alpha-waarde(doorzichtbaarheid) kan hebben waardoor de game over blok doorzichtig kan zijn!
        game_over_blok = pygame.Surface((game_over_rect.width, game_over_rect.height), pygame.SRCALPHA)
        #Vul de surface met een transparante grijze kleur met een alpha van 150
        game_over_blok.fill((50, 50, 50, 150))
        settings.screen.blit(game_over_blok, game_over_rect.topleft)
        # Teken een zwarte rand rond het game-over scherm
        pygame.draw.rect(settings.screen, settings.black, game_over_rect, 5)

        # Tekst weergeven
        score_text = settings.font.render("Appels gegeten: {}".format(appel_score), True, settings.white)
        score_text_rect = score_text.get_rect(center=(400, 260))
        settings.screen.blit(score_text, score_text_rect)

        lose_text = settings.font.render("Je hebt verloren!", True, settings.white)
        lose_text_rect = lose_text.get_rect(center=(400, 200))
        settings.screen.blit(lose_text, lose_text_rect)
        # Teken de knop "Opnieuw spelen"
        if button.draw(250, 300, 300, 50, "Opnieuw spelen", settings.green, settings.white):
            gf.reset()  # Reset het spel en de slang
            game_over = False  # Zet game_over naar False zodat het spel doorgaat
            snake.clear()
            snake_head = Snake_piece(0)
            # de eerste lichaamsdelen
            snake1 = Snake_piece(1)
            snake.append(snake1)
            snake2 = Snake_piece(2)
            snake.append(snake2)
            snake3 = Snake_piece(3)
            snake.append(snake3)
            speed=settings.spel_snelheid
            apple_x, apple_y = apple.new_pos()
            #reset appel/score teller
            appel_score = 0
            moves_list = []
            music_sfx.play()
            
        if button.draw(250, 375, 300, 50, "Sluiten", settings.red, settings.white):
            running = False #Het hele scherm wordt dan gesloten als er op de knop wordt gedrukt.

    pygame.display.flip()  # Werk het scherm bij
    clock.tick(speed)  # Beperk de framesnelheid tot de ingestelde snelheid

pygame.quit()
