import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adding a rectangle")
pygame.draw.circle(screen, (0, 225, 0), (100, 200), 50)
pygame.draw.circle(screen, (0, 225, 0), (300, 300), 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            running = False
    pygame.display.flip()