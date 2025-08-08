import pygame


pygame.init()

WIDTH,HEIGHT = 512 ,512
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

player = pygame.Rect((0,0,50,50))
player1 = pygame.Rect((50,0,50,50))
run = True
while run:

    WIN.fill((0,0,0))

    pygame.draw.rect(WIN,(255,0,0),player)
    pygame.draw.rect(WIN, (255, 0, 0), player1)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    if key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)
    if key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    if key[pygame.K_DOWN] == True:
        player.move_ip(0,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()


