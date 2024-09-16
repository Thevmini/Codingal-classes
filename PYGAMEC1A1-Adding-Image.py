import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

img = pygame.transform.scale(pygame.image.load("toothless (1).png"), (400, 500))
bg_img = pygame.transform.scale(pygame.image.load("grass (2).png"), (400, 500))

test_font = pygame.font.Font(None, 60)
text = test_font.render("Pygame Introduction", True, pygame.Color("white"))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(bg_img, (0,0))
    screen.blit(img, (0,0))
    screen.blit(text, (20,400))
    pygame.display.flip()