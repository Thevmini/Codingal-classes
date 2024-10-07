import pygame
import random
import math

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("background.jpeg")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.jpeg")
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load("player.jpeg")
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
plyer_x_change = 0

# enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_enemies = 6

for i in range(num_enemies):
    enemy_img.append(pygame.image.load("enemy.jpeg"))
    enemy_x.append(random.randint(0, SCREEN_WIDTH-64))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)

# bullet
bullet_img = pygame.image.load("bullet.jpeg")
bullet_x = 0
bullet_y = PLAYER_START_X
bullet_x_change = 0
bullet_y_change = BULLET_SPEED_Y
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font("super_unicorn.ttf", 64)
