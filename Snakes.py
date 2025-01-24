import pygame

# Initialiseer pygame
pygame.init()

# Scherm instellen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snakes")

#Kleur en klok instellen
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Slang variabele
x = 300
y = 250
snelheid = 25
left = False
right = False
up = False
down = False

# Hoofdlus
running = True
game_over = False

def draw_button(x, y, w, h, text, color, text_color):
    #Tekent een knop en retourneert True als erop geklikt is.
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Controleer of de muis binnen de knop is
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, color, (x, y, w, h))
        if click[0] == 1:  # Linkermuisknop ingedrukt
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, w, h), 2)

    # Voeg tekst toe aan de knop
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surface, text_rect)

    return False

while running:
    screen.fill(black)  #Vul de achtergrond met zwart

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Beweeg de slang alleen als het spel niet over is
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not down:
                up = True
                left = right = False
            elif event.key == pygame.K_DOWN and not up:
                down = True
                left = right = False
            elif event.key == pygame.K_LEFT and not right:
                left = True
                up = down = False
            elif event.key == pygame.K_RIGHT and not left:
                right = True
                up = down = False

    if not game_over:
        # Beweeg de slang
        if left:
            x -= snelheid
        if right:
            x += snelheid
        if up:
            y -= snelheid
        if down:
            y += snelheid

        # Controleer of de slang buiten het scherm gaat
        if x >= 800 or x < 0 or y >= 600 or y < 0:
            game_over = True

        # Teken de slang
        pygame.draw.rect(screen, green, (x, y, 25, 25))
    else:
        # Teken het groene vierkant en de tekst
        game_over_rect = pygame.Rect(150, 200, 500, 150)
        pygame.draw.rect(screen, green, game_over_rect)

        lose_text = font.render("Jij hebt dit spel verloren", True, white)
        lose_text_rect = lose_text.get_rect(center=game_over_rect.center)
        screen.blit(lose_text, lose_text_rect)
        
        if draw_button(200, 400, 400, 50, "Opnieuw starten", red, white):
            # Reset de spelstatus
            x = 300
            y = 250
            left = right = up = down = False
            game_over = False

    pygame.display.flip()  # Werk het scherm bij
    clock.tick(5)  # Beperk de framesnelheid tot 30 FPS

pygame.quit()
