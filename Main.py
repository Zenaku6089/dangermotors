import pygame

class Jogador(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("data\person.png")
        self.rect=self.sprite.get_rect()
        self.rect.x=0
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
dimensao=(1200,700)
bg_w, bg_h = dimensao 
bg = pygame.transform.smoothscale(pygame.image.load('data/fase01.png'), (bg_w, bg_h))
pos_x = 0
speed = 10

screen=pygame.display.set_mode(dimensao)
X=1200
Y=700
x=400
y=430
x2=30
y2=100

sta1=pygame.image.load("Data/f1.png")
sta2=pygame.image.load("Data/f2.png")
sta3=pygame.image.load("Data/f3.png")
lock=pygame.image.load("Data/locker1.png")
lock2=pygame.image.load("Data/locker1.png")
block=True
block2=True

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

 
def Select():
    screen.fill((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 30)
 
    text1 = font.render('Nível 1', True, "white")


    textr1 = text1.get_rect()
 

    textr1.center = (200, 100)
    text2 = font.render('Nível 2', True, "white")


    textr2 = text2.get_rect()
 

    textr2.center = (200,300)
    text3 = font.render('Nível 3', True, "white")


    textr3 = text3.get_rect()
 

    textr3.center = (200,500)
    selectm = font.render('Selecione Nível', True, "white")

    selectmr = selectm.get_rect()
      

    selectmr.center = (X//2,25)     
    screen.blit(text1, textr1)
    screen.blit(text2, textr2)
    screen.blit(text3, textr3)
    screen.blit(selectm, selectmr)
    screen.blit(sta1,(600,70))
    screen.blit(sta2,(600,270))
    screen.blit(sta3,(600,470))
    
    pygame.display.flip()  
running=True
ativo=False
levelzinho="Nivel1"
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
               ativo=False
            
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
                allKeys = pygame.key.get_pressed()
                pos_x += speed if allKeys[pygame.K_LEFT] else -speed if allKeys[pygame.K_RIGHT] else 0

                x_rel = pos_x % bg_w
                x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w

                screen.blit(bg, (x_rel, 0))
                screen.blit(bg, (x_part2, 0))
            
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
                   
            if status=="seleção":
             Select()
           
             pygame.draw.rect(screen, (2,84,80), (x2,y2, 20,20))
             
             if block==True:
                 screen.blit(lock,(600,270))
                 lock2.set_alpha(128)
             if block2==True:
                 screen.blit(lock2,(600,470))
                 lock.set_alpha(128)
             '''if pontos1!=0:
                 block=False
             if pontos2!=0:
                 block2=False'''
             if e.type == pygame.KEYDOWN and e.key == pygame.K_UP  :
                if y2>300:
                   y2=300
                else:
                    y2=100
             if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN  :
                if y2<300:
                   y2=300
                else:
                    y2=500
             if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and y2==100:
                 
                
                 levelzinho="Nível 1"
                 
             if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and y2==300 :
                 
                 levelzinho="Nível 2"
                 
              
                  
             if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and y2==500 :
                 
                 levelzinho="Nível 3"
            
            if ativo:
            
             key = pygame.key.get_pressed()
             if key[pygame.K_LEFT]:
                if jogador.rect.x>0:
                  jogador.move((-20), 0)
                else:
            
                  jogador.move((2), 0)
                  
             if key[pygame.K_RIGHT]:
                 if jogador.rect.x<700 :
                     jogador.move(20, 0)
                 else:
                     jogador.move((-2), 0) 
            
          
               
            
            pygame.display.flip()
pygame.quit()

