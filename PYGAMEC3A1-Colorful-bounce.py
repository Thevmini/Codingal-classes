import random
import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Colorful Bounce")

sprite_color_change_event = pygame.USEREVENT+1
bg_color_change_event = pygame.USEREVENT+2

red = pygame.Color("red")
green = pygame.Color("green")
blue = pygame.Color("blue")
yellow = pygame.Color("yellow")
white = pygame.Color("white")
orange = pygame.Color("orange")
magenta = pygame.Color("magenta")

bg_color = blue
sp_color = white
screen.fill(bg_color)

clock = pygame.time.Clock()

def change_bg_color():
    global bg_color
    bg_color = random.choice([blue, green, magenta])

def change_sp_color(sprite):
    new_color = random.choice([blue, green, magenta])
    sprite.change_color(new_color)

all_sprites_group = pygame.sprite.Group()
running = True

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]

        if self.rect.top<=0 or self.rect.bottom>=500:
            self.velocity[1]=-self.velocity[1]

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(bg_color_change_event))

    def change_color(self, new_color):
        self.image.fill(new_color)

sp1 = Sprite(sp_color, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 470)
all_sprites_group.add(sp1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            running = False
        elif event.type == bg_color_change_event:
            change_bg_color()
        elif event.type == sprite_color_change_event:
            change_sp_color(sp1)
    all_sprites_group.update()
    screen.fill(bg_color)
    all_sprites_group.draw(screen)
    clock.tick(90)
    pygame.display.flip()
pygame.quit()