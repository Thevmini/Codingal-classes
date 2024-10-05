import pygame
import random

pygame.init()

screen_width, screen_height = 500, 500
font_size = 72
won = False
screen = pygame.display.set((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision")

bg_img = pygame.transform.scale(pygame.image.load("collision.jpeg"), (screen_width, screen_height))

font = pygame.font.SysFont("Times New Roman", font_size)

def create_sprite(color, width, height):
    sprite = pygame.Surface([width, height])
    sprite.fill(pygame.Color("dodgerblue"))
    pygame.draw.rect(sprite, color, pygame.Rect (0, 0, width, height))
    rect = sprite.get_rect()
    rect.x - random.randint(0, screen_width-rect.width)
    rect.y - random.randint(0, screen_height-rect.height)
    return sprite, rect

def move_sprite(rect, x_change, y_change):
    rect.x = max(0, min(rect.x+x_change, screen_width-rect.width))
    rect.x = max(0, min(rect.y+y_change, screen_height-rect.height))


sprite1, rect1 = create_sprite(pygame.Color("black"), 30, 30)
sprite2, rect2 = create_sprite(pygame.Color("red"), 30, 30)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            running = False
        if not won:
            keys = pygame.key.get_pressed()
            x_change += keys[pygame.K_RIGHT] - (keys[pygame.K_LEFT]*5)
            y_change += keys[pygame.K_DOWN] - (keys[pygame.K_UP]*5)

            move_sprite(rect1, x_change, y_change)

        screen.blit(bg_img, (0, 0))
        screen.blit(sprite1, rect1.topleft)
        screen.blit(sprite2, rect2.topleft)

        if won:
            win_text = font.render("You win!!", True, pygame.Color("black"))
            screen.blit(
                win_text,
                (
                    (screen_width-win_text.get_width())//2,
                    (screen_height-win_text.get_height())//2
                )
            )

    pygame.display.flip()
    clock.tick(90)
pygame.quit()