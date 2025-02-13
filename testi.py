import pygame
from random import randint,choice

class Solu:
    def __init__(self, xy: tuple):
        self.xy = xy
        self.naapurit = []
        self.osat = []
        self.kayty = False

    def lisaa_naapuri(self, naapurixy: tuple):
        self.naapurit.append(naapurixy)
    
    def lisaa_osat(self, osat: list):
        self.osat = osat
    

class osa:
    def __init__(self):
        self.yla = yla
        self.ala = ala
        self.vasen = vasen
        self.oikea = oikea    



    


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

def luo_naapurit(syote): # luo naapurit jokaiselle osalle
    osat = {}
    
    for i in range(len(syote)):
        osat[i] = {"yla": [], "ala": [], "vasen": [], "oikea": []}
        for j in range(len(syote)):    
            osat[i]["yla"].append(j)
            osat[i]["ala"].append(j)
            osat[i]["vasen"].append(j)
            osat[i]["oikea"].append(j)


    for i in range(len(syote)):
        for j in range(len(syote)):
            if not on_sama(syote[i].subsurface(0, 1, 3, 2), syote[j].subsurface(0, 0, 3, 2)):
                osat[i]["ala"].remove(j)
            if not on_sama(syote[i].subsurface(0, 0, 2, 3), syote[j].subsurface(1, 0, 2, 3)):
                osat[i]["vasen"].remove(j)
            if not on_sama(syote[i].subsurface(1, 0, 2, 3), syote[j].subsurface(0, 0, 2, 3)):
                osat[i]["oikea"].remove(j)
            if not on_sama(syote[i].subsurface(0, 0, 3, 2), syote[j].subsurface(0, 1, 3, 2)):
                osat[i]["yla"].remove(j)
     
    return osat

def on_sama(kuva1, kuva2):
    for y in range(kuva1.get_height()):
        for x in range(kuva1.get_width()):
            if kuva1.get_at((x, y)) != kuva2.get_at((x, y)):
                return False
    return True


osat = pilko(box)
lista = luo_naapurit(osat)
print(on_sama(osat[0], osat[0]))
print(lista[40])
print(list(range(0,10)))


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
    
    