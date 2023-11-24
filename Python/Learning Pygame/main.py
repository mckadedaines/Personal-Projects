# There are 3 important things you need when creating a game in pygames.
# 1. Game Window
# 2. Game Loop
# 3. Game Event Handler

import pygame

# Game Window
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

player =  pygame.Rect((300, 250, 50, 50))

# Game Loop
run = True
while run:

# This removes the smudging of the players color so its not trash
    screen.fill((0, 0, 0))

# This draws the player on the screen
    pygame.draw.rect(screen, (255, 0, 0), player)

# This is how you can make the player move
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    if player.left < 0:
        player.left = 0
    elif player.right > screen_width:
        player.right = screen_width
    elif player.top <= 0:
        player.top = 0
    elif player.bottom >= screen_height:
        player.bottom = screen_height

# Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# This constantly updates pygames to show your character
    pygame.display.update()

pygame.quit()