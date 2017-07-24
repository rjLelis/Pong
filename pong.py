import pygame, colors
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32) # Tamanho da tela

pygame.display.set_caption('Pong') # Título do jogo

font = pygame.font.SysFont('Calibri', 50, True, False) # Fonte do jogo

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

ball_list = []

def create_ball(): # Função de criar a "bola"
    return { # atributos da "bola"
        'surface': [20, 25],
        'position':[478, 210],
        'speed': {
            'x': 5,
            'y': -5
            }
        }

def remove_ball(): # Função de remover a "bola"
    for ball in ball_list:
        if ball['position'][0] > 956 or ball['position'][0] < 0:
            ball_list.remove(ball)

clock = pygame.time.Clock()

stantart_player_speed = 7 # velocidade dos jogadores

done = False

while not done:

    player1['speed']['y'] = 0
    player2['speed']['y'] = 0

    if len(ball_list) == 0:
        ball_list.append(create_ball())
    
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

    # ---- Desenhos e movimentos que aparecem na tela ---- #
    
    screen.fill(colors.BLACK)

    score_player1 = font.render(str(player1['score']), True, colors.WHITE)
    screen.blit(score_player1, [20, 15])

    score_player2 = font.render(str(player2['score']), True, colors.WHITE)
    screen.blit(score_player2, [905, 15])

    pygame.draw.line(screen, colors.BLUE, [478,0], [478,560], 5)
    
    for ball in ball_list:
        pygame.draw.rect(screen, colors.WHITE, [ball['position'], ball['surface']])
        
    ball['position'][0] += ball['speed']['x']
    ball['position'][1] += ball['speed']['y']

    pygame.draw.rect(screen, colors.WHITE,[player1['position'], player1['surface']])
    pygame.draw.rect(screen, colors.WHITE, [player2['position'], player2['surface']])

    # ---- Colisões ---- #
   
    if ball['position'][1] > 535 or ball['position'][1] < 0:
        ball['speed']['y'] *= -1

    if ball['position'][0] > 956:
        player1['score'] += 1
    elif ball['position'][0] < 0:
        player2['score'] += 1

    remove_ball()

    # ---- Atualizar a tela do jogo ---- #

    pygame.display.flip()
    
    clock.tick(30)
    
pygame.quit()
