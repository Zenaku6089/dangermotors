import pygame


pygame.init()
tela=pygame.display.set_mode((800,600))
menuImage=pygame.image.load()

tela.fill((255,0,0))
icon=pygame.image.load()
pygame.display.set_icon(icon)
tela.blit(menuImage,())

pygame.display.update()


