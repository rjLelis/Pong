import pygame, colors
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    '''
    Player class
    '''
    def __init__(self, color, width, height, x, y):

        super().__init__()

        self.image = pygame.Surface([width, height])

        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.x_pos = x

        self.y_pos = y

        self.x_speed = 5

        self.y_speed = -5

        self.score = 0

def main():
    
    '''Main Function'''
    
    pygame.init()

    screen = pygame.display.set_mode((956, 560)) # Screen size

    pygame.display.set_caption('Pong') # Game title

    font = pygame.font.SysFont('Calibri', 50, True, False) # Game font

    player1 = Player(colors.WHITE, 20, 90, 5, 99) # Left player attributes

    player2 = Player(colors.WHITE, 20, 90, 930, 210) # Right player attributes

    ball_list = []

    def create_ball():
        '''Returns the ball attributes to be drawn in the screen'''
        return { # Ball attributes
            'surface': [20, 25],
            'position':[478, 210],
            'speed': {
                'x': 5,
                'y': -5
                }
            }

    def remove_ball():
        '''Removes the ball from the game'''
        for ball in ball_list:
            if ball['position'][0] > 956 or ball['position'][0] < 0:
                ball_list.remove(ball)

    clock = pygame.time.Clock()

    stantart_player_speed = 7 # Stantart players speed

    done = False

    while not done:

        player1.y_speed = 0
        player2.y_speed = 0

        if len(ball_list) == 0:
            ball_list.append(create_ball())
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        # ---- Players moviments ---- #
        
        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_w]:
            player1.y_speed = stantart_player_speed * (-1)
        elif pressed_key[K_s]:
            player1.y_speed = stantart_player_speed   

        if pressed_key[K_UP]:
            player2.y_speed = stantart_player_speed * (-1)
        elif pressed_key[K_DOWN]:
            player2.y_speed = stantart_player_speed

        player1.y_pos += player1.y_speed
        player2.y_pos += player2.y_speed

        # ---- Drawings and moviments that appear on the screen ---- #
        
        screen.fill(colors.BLACK)

        pygame.draw.line(screen, colors.BLUE, [478,0], [478,560], 5)

        screen.blit(player1.image, (player1.x_pos,player1.y_pos))

        screen.blit(player2.image, (player2.x_pos, player2.y_pos))

        score_player1 = font.render(str(player1.score), True, colors.WHITE)
        screen.blit(score_player1, [20, 15])

        score_player2 = font.render(str(player2.score), True, colors.WHITE)
        screen.blit(score_player2, [905, 15])
        
        for ball in ball_list:
            pygame.draw.rect(screen, colors.WHITE, [ball['position'], ball['surface']])
            
        ball['position'][0] += ball['speed']['x']
        ball['position'][1] += ball['speed']['y']

        # ---- Colisions ---- #
       
        if ball['position'][1] > 535 or ball['position'][1] < 0:
            ball['speed']['y'] *= -1

        if ball['position'][0] > 956:
            player1.score += 1
        elif ball['position'][0] < 0:
            player2.score += 1

        remove_ball()

        # ---- Atualizar a tela do jogo ---- #

        pygame.display.flip()
        
        clock.tick(30)
        
    pygame.quit()

if __name__ == '__main__':
    main()
