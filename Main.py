import pygame

class Jogador(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("data\person.png")
        self.rect=self.sprite.get_rect()
        self.rect.x=1200//2
        self.rect.y=150
  

    def draw(self, surface):
       surface.blit(self.sprite, (self.rect.x, self.rect.y))

    def move(self, dx, dy):
        
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
     
        
        self.rect.x += dx
        self.rect.y += dy

pygame.init()

screen=pygame.display.set_mode((1200,700))
X=1200
Y=700
x=400
y=430

status="menu"
def Menu():
    #icon=pygame.image.load("Data/icon.ico")
    #pygame.display.set_icon(icon)
    imagem=pygame.image.load("Data/menu2.jpg")
    screen.blit(imagem,(-50,-100))
    #font = pygame.font.Font('White On Black.ttf', 40)
    #fonte = pygame.font.Font('White On Black.ttf', 90)
    font = pygame.font.Font('freesansbold.ttf', 40)
    fonte = pygame.font.Font('freesansbold.ttf', 90)
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
ativo=False
jogador=Jogador()
while running:

   
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
              running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
              running = False
              
    
       
              
            if status=="menu":
               jogador=Jogador()
               Menu()
               
            
               pygame.draw.rect(screen, (2,84,80), (x,y, 20,20))
               if e.type == pygame.KEYDOWN and e.key == pygame.K_UP :
                 x=400
                 y=430
            
               if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN  :
                 x=400
                 y=530
            
           
               pygame.display.flip()

               
            if status=="jogo":
                screen.fill('red')
                fase1=pygame.image.load("Data/fase01.png")
                screen.blit(fase1,(10,10))
                jogador.draw(screen)
           

                
            if status=="seleção":
                
                fase1=pygame.image.load("Data/fase01.png")
                screen.blit(fase1,(0,0))

                
            if y==430 and e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                   
                  
                   status="jogo"
                   ativo=True
            if y==530 and e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                
                   screen.fill('yellow')
                   status="seleção"
                   
            if e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE :
                   status="menu"
            if ativo:
            
             key = pygame.key.get_pressed()
             if key[pygame.K_LEFT]:
                jogador.move((-20), 0)
             if key[pygame.K_RIGHT]:
                jogador.move(20, 0)
             if key[pygame.K_UP]:
                y=100
             else:
                y=150
                jogador.move((-2), 0) 
             
            pygame.display.flip()
pygame.quit()

