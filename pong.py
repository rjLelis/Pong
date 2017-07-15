import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)

pygame.display.set_caption('Pong')

background_filename = 'cross.png'

background = pygame.image.load(background_filename).convert()

player1 = {
    'surface': pygame.image.load('player.png').convert_alpha(),
    'position': [5, 210],
    'speed': {
        'x': 0,
        'y': 0
        }
    }

player2 = {
    'surface': pygame.image.load('player.png').convert_alpha(),
    'position': [925, 210],
    'speed': {
        'x': 0,
        'y': 0
        }
    }

clock = pygame.time.Clock()

standart_speed = 7

while True:

    player1['speed']['y'] = 0
    player2['speed']['y'] = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_key = pygame.key.get_pressed()

    if pressed_key[K_w]:
        player1['speed']['y'] = standart_speed * (-1)
    elif pressed_key[K_s]:
        player1['speed']['y'] = standart_speed

    if pressed_key[K_UP]:
        player2['speed']['y'] = standart_speed * (-1)
    elif pressed_key[K_DOWN]:
        player2['speed']['y'] = standart_speed

    player1['position'][1] += player1['speed']['y']
    player2['position'][1] += player2['speed']['y']

    screen.blit(background, (0, 0))

    screen.blit(player1['surface'], player1['position'])
    screen.blit(player2['surface'], player2['position'])

    pygame.display.update()
    time_passed = clock.tick(30)
