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
#vai guardar as dimençoes da tela
dimensao=(1200,700)
bg_w, bg_h = dimensao

gameover=pygame.image.load("Data/gameover.jpg")
fase1='data/fase01.png'

#vai carregar a imagem do cenario
bg = pygame.transform.smoothscale(pygame.image.load(fase1), (bg_w, bg_h))
pos_x = 0
speed = 10

screen=pygame.display.set_mode(dimensao)
X=1200
Y=700

#coordenadas do ponteiro da tela principal
x=400
y=430

#coordenadas do ponteiro da tela de seleção
x2=30
y2=100

#miniatura das fases
sta1=pygame.image.load("Data/f1.png")
sta2=pygame.image.load("Data/f2.png")
sta3=pygame.image.load("Data/f3.png")

#cadeado para simbolisar que não esta liberada ainda
lock=pygame.image.load("Data/locker1.png")
lock2=pygame.image.load("Data/locker1.png")
block=True
block2=True

#variaveis de entrada de texto de pontuaçao
text = ""
input_active = True
font = pygame.font.SysFont(None, 100)
#esta variavel é uma flag para medir quanto o player percorreu
ponto=0
score=''
#status vai controlar qual tela esta sendo selecionada
status="menu"

#configurações de audio
musica1 = pygame.mixer.Sound("data/musica1.mp3")
musica1.set_volume(0.40)

musica2 = pygame.mixer.Sound("data/musica2.mp3")
musica2.set_volume(0.40)

#função para mostrar texto na tela
def textinho(texto,x,y,tamanho):
    
    
 
    font=pygame.font.Font('freesansbold.ttf', tamanho)
    text = font.render(texto, True, "black")
   

    textRect = text.get_rect()

    textRect.center = (x,y)
    screen.blit(text, textRect)

# função do menu
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

#função da tela de seleção 
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
               musica1.play(-1, 0, 1000)
               musica2.stop()
               jogador=Jogador()
               Menu()
               ponto=0
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
                musica2.play(-1, 0, 1000)
                musica1.stop()
                screen.fill('red')
                allKeys = pygame.key.get_pressed()
                pos_x += speed if allKeys[pygame.K_LEFT] else -speed if allKeys[pygame.K_RIGHT] else 0
               
                x_rel = pos_x % bg_w
                x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w

                #condicionais da flag ponto
                if allKeys[pygame.K_RIGHT] :
                     ponto=ponto+1
                if allKeys[pygame.K_LEFT] :
                     ponto=ponto-1
                
                print(ponto)
                screen.blit(bg, (x_rel, 0))
                screen.blit(bg, (x_part2, 0))
            
                jogador.draw(screen)
           

                
            if status=="seleção":
                
                fase1=pygame.image.load("Data/fase01.png")
                screen.blit(fase1,(0,0))

                
            if y==430 and e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and status=="menu":
                   
                  
                   status="jogo"
                   ativo=True
            if y==530 and e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and status=="menu":
                
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


                 
            if ponto==100:
                status="gameover"
                
            if status=="gameover":
               ativo=False
               screen.fill('pink')
               screen.blit(gameover,(0,0))
               score=str(ponto)
               if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                   status="pontuação"

            if status=="pontuação":
                ponto=0
                ativo=False
                screen.fill('pink')
                textinho("Pontuação",(1200//2),(700//1.5),48)
                textinho(score,(1200//2),(700//1.7),48)
               
                
                    
           
                if e.type == pygame.KEYDOWN and e.type == pygame.K_SPACE :
                
                 textinho("Digite o seu nome",(1200//2),(700//1.9),48)
                 input_active = True
                 text = " " # a variavel text é declada vazia
               
                if e.type ==pygame.KEYDOWN and input_active:
                      if e.type == pygame.K_RETURN:#esse comando confirma o nome RETURN é o mesmo que a tecla ENTER)
                           input_active = False
                      elif e.key == pygame.K_DELETE:# esse comando permite apagar as letras
                           text =  text[:-1]
                      else:
                           text += e.unicode#esse comando grava as letras dentro da variavel text
                text_surf = font.render(text, True, (255, 0, 0)) # define a fonte, o texto, e a cor
                screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))# exibe             
    
                if e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE:
                    status="menu"
                    cheio=text.len()
                    text=text[:-cheio]
               
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

