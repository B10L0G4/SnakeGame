import  pygame #importa a biblioteca do pygame 
import random
from pygame.locals import*

def on_grid_random():#para alinhar a maçã e a snake
    x = random.randint(0, 590) 
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10 )

def collision(c1, c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1])) #colisão da cobra com a maçã 

UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

pygame.init # necessário para iniciar o pygame 
screen = pygame.display.set_mode((600,600)) # set de tela 
pygame.display.set_caption("Snake")

snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10)) #para cada posição da snake
snake_skin.fill((255,255,255)) #define a cor da minha snake , rgb para branco 

apple_pos = on_grid_random() # 590 valor máximo para não sair da tela 
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #fator rgb vermelho , cor da maçã

my_direction = LEFT  #COMEÇA INDO PARA ESQUERDA 

clock = pygame.time.Clock() #movimento da snake

pygame.font.init() #inicialização de score 
font = pygame.font.Font('freesansbold.ttf', 22) 
score = 0

while True: #todo jogo tem um laço infinito , com eventos de mudança , toque ou cliques
    clock.tick(10) #limitação de FPS
    for event in pygame.event.get(): # evento para fechamento do jogo (1° evento )
        if event.type == QUIT:
            pygame.quit()
         
        if event.type ==KEYDOWN: #controle de movimentos , teclas  ( 2° evento)
           if event.key == K_UP:
                my_direction = UP
           if event.key == K_DOWN:
                my_direction = DOWN
           if event.key == K_LEFT:
                my_direction = LEFT
           if event.key == K_RIGHT:
                my_direction = RIGHT           
     
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random() #gera uma nova posição para a maçã
        snake.append((0,0)) #nova posição para a cobra, aumento de tamanho
        score = score + 1 #incremento de score
        
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0: #verifica a colisão da snake com as bordas
        pygame.quit()
        exit()
    for i in range (1, len(snake) - 1): # verifica a colisão da snake com a snake
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()
            exit()
              
    for i in range(len(snake)-1, 0, -1):# laço para mover o corpo, recebe a posição da calda anterior 
        snake[i] = (snake[i -1][0], snake[i-1][1])

    if my_direction == UP: # movento direcional da cabeça 
        snake[0] = (snake[0][0],snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] +10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -10,snake[0][1])
        
    screen.fill([0,0,0]) #limpa a tela 
    screen.blit(apple,apple_pos)
    
    for x in range(0,600,10) : #desenha linhas verticais 
        pygame.draw.line(screen, (100,100,150), (x, 0), (x, 600))
    for y in range(0,600,10) : #desenha linhas verticais 
        pygame.draw.line(screen, (40,40,40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255,255,255)) 
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 -580, 20)
    screen.blit(score_font, score_rect)
        
    for pos in snake:
        screen.blit(snake_skin, pos)
    
    pygame.display.update()