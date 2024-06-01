import pygame
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

kvadrati = []
for x in range(0, 600, 200):
    for y in range(0,600,200):
        r = pygame.Rect(x + 400, y + 100,200,200)
        kvadrati.append(r)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for k in kvadrati:
        pygame.draw.rect(screen, 'black', k,5)


    pygame.display.flip()

    clock.tick(60)
pygame.quit()


