import pygame


pygame.init()

screen=pygame.display.set_mode((1200,700))
X=1200
Y=700
x=400
y=430
def Menu():
    icon=pygame.image.load("Data\icon.ico")
    pygame.display.set_icon(icon)
    imagem=pygame.image.load("Data/menu2.jpg")
    screen.blit(imagem,(-50,-100))
    font = pygame.font.Font('White On Black.ttf', 40)
    fonte = pygame.font.Font('White On Black.ttf', 90)
    fontCredito = pygame.font.Font('freesansbold.ttf', 15)


    textm = font.render('Iniciar Jogo', True, "white")

    textRectm = textm.get_rect()
 
    textRectm.center = (X // 2,450)
    screen.blit(textm, textRectm)
    texts = font.render('Selecionar Fase', True, "white")


    textRects = texts.get_rect()
 

    textRects.center = (X // 2,550)
    screen.blit(texts, textRects)
    texttt = fonte.render('DANGERMOTORS ', True,(2,84,80))


    textRecttt = texttt.get_rect()
 

    textRecttt.center = (X // 2,100)
    screen.blit(texttt, textRecttt)
    texttt3 = fontCredito.render('[Aperte Space]', True, (2,84,80))


    textRecttt3 = texttt3.get_rect()
 

    textRecttt3.center = (1100,650)
    screen.blit(texttt3, textRecttt3)
   
    textttc = fontCredito.render('By Vinicius,Walef,Italo (2025)', True, "white")


    textRectttc = textttc.get_rect()
 

    textRectttc.center = (X // 2,650)
    screen.blit(textttc, textRectttc)


running=True
while running:
    Menu()
    pygame.draw.rect(screen, (2,84,80), (x,y, 20,20))
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
              running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
              running = False
              pygame.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP :
               x=400
               y=430
            
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN  :
               x=400
               y=530
    pygame.display.flip()
