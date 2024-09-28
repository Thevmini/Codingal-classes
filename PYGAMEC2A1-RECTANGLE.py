import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adding a rectangle")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            running = False
    pygame.draw.rect(screen, (10, 125, 125), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()