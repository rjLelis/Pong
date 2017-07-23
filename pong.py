import pygame
from pygame.locals import *
import colors

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)

pygame.display.set_caption('Pong')

font = pygame.font.SysFont('Calibri', 50, True, False)

player1 = { # Atributos do jogador á esquerda
    'surface': [20, 99],
    'position': [5, 210],
    'speed': {
        'x': 0,
        'y': 0
        },
    'score': 0
    }

player2 = { # Atributos do jogador á direita
    'surface': [20, 99],
    'position': [930, 210],
    'speed': {
        'x': 0,
        'y': 0
        },
    'score': 0
    }

ball = { # atributos da "bola"
    'surface': [20, 25],
    'position':[478, 210],
    'speed': {
        'x': 5,
        'y': 5
        }
    }

clock = pygame.time.Clock()

stantart_player_speed = 7 # velocidade dos jogadores

done = False

while not done:

    player1['speed']['y'] = 0
    player2['speed']['y'] = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # ---- Movimentação dos jogadores ---- #
    
    pressed_key = pygame.key.get_pressed()

    if pressed_key[K_w]:
        player1['speed']['y'] = stantart_player_speed * (-1)
    elif pressed_key[K_s]:
        player1['speed']['y'] = stantart_player_speed

    if pressed_key[K_UP]:
        player2['speed']['y'] = stantart_player_speed * (-1)
    elif pressed_key[K_DOWN]:
        player2['speed']['y'] = stantart_player_speed

    player1['position'][1] += player1['speed']['y']
    player2['position'][1] += player2['speed']['y']

    # ---- Desenhos que aparecem na tela ---- #
    
    screen.fill(colors.BLACK)

    score1 = font.render(str(player1['score']), True, colors.WHITE)
    screen.blit(score1, [20, 20])

    score2 = font.render(str(player2['score']), True, colors.WHITE)
    screen.blit(score2, [910, 20])

    pygame.draw.line(screen, colors.BLUE, [478,0], [478,560], 5)
    
    pygame.draw.rect(screen, colors.WHITE, [ball['position'], ball['surface']])
    #ball['position'][0] += ball['speed']['x']
    #ball['position'][1] += ball['speed']['y']

    pygame.draw.rect(screen, colors.WHITE,[player1['position'], player1['surface']])
    pygame.draw.rect(screen, colors.WHITE, [player2['position'], player2['surface']])

    # ---- Colisões ---- #
   
    if ball['position'][1] > 535 or ball['position'][1] < 0:
        ball['speed']['y'] *= -1

    pygame.display.update()
    
    clock.tick(30)
    
pygame.quit()
