import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

bg_img = pygame.transform.scale(pygame.image.load("toothless (1).png"), (400, 500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(bg_img, (0,0))
    pygame.display.flip()