import pygame
from random import randint,choice

class Solu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.naapurit = []
        self.osat = []
        self.vari = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.kayty = False



    


pygame.init()
leveys = 600
korkeus = 600

naytto = pygame.display.set_mode((leveys, korkeus))
ruudut = []
osat = []
box = pygame.Surface((9, 9))
box.fill((255, 255, 255))
pygame.draw.rect(box, (0, 0, 0), (1, 1, 7, 7))  # Black border
pygame.draw.rect(box, (255, 0, 0), (2, 2, 5, 5))  # Red interior



def pilko(lahde): # pilkkoo kuvan 3x3 osiin
    osat = []
    
    for y in range(lahde.get_height()):
        for x in range(lahde.get_width()): 
            osa = pygame.Surface((3, 3))
            for j in range(3):
                for i in range(3):
                    osa.set_at((i, j), lahde.get_at(((x+i)%lahde.get_width(), (y+j)%lahde.get_height())))
            osat.append(osa)
    return osat


osat = pilko(box)
koko = leveys//box.get_width()/3
naytto.fill((255, 255, 255))
for i in range(len(osat)):
    x = i%box.get_width()
    y = i//box.get_height()
    for k in range(9):
        pygame.draw.rect(naytto, (0,0,0), (x*3*koko+k%3*koko, y*3*koko+k//3*koko, koko , koko))
        pygame.draw.rect(naytto, (osat[i].get_at((k%3,k//3))), (x*3*koko+k%3*koko+1, y*3*koko+k//3*koko+1, koko-2 , koko-2))

    
pygame.display.flip()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    