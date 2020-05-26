import pygame 
import random

#Inicia o pygame
pygame.init()

#Cria a tela. ((width,height))
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.png')

#Titulo e Icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
#Ready -> não consegue ver a bala na tela
#Fire -> A bala esta se movendo
bullet_state = "ready"

def player(x, y):
    #desenhando a imagem do player
    screen.blit(playerImg,(x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

#Game Loop
running = True
while running:

    #RGB
    screen.fill((0,0,0))
    #Background image
    screen.blit(background, (0, 0)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checando se estamos pressionando para direita ou esquerda no teclado
        if event.type == pygame.KEYDOWN:
            print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                

    # Chechando pelos limites da tela, evitando que a nave e o inimigo saiam da tela.
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    #800-64 (largura da nave)
    elif playerX >= 736:
        playerX = 736

    
    #Movimento do inimigo.
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2
        enemyY+= enemyY_change

    #Movimento da bala.
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change
        
    #800-64 (largura da nave)
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY+= enemyY_change

        

    

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
            
