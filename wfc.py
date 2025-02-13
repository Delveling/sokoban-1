class Ruudukko:
    def __init__(self, leveys: int, korkeus: int, osat: int):
        self.leveys = leveys
        self.korkeus = korkeus
        self.r = [list(range(osat)) for _ in range(leveys*korkeus)]
        self.valmis = [False for _ in range(leveys*korkeus)]
    
    def tulosta(self):
        for y in range(self.korkeus):
            for x in range(self.leveys):
                print(self.r[y*self.leveys + x], end="")
            print()
    
    def pituudet(self):
        for y in range(self.korkeus):
            for x in range(self.leveys):
                print(len(self.r[y*self.leveys + x]), end="")
            print()

    def palauta(self,xy: tuple):
        try:
            return self.r[int(xy[1])*self.leveys + int(xy[0])]
        except:
            try:
                return self.r[int(xy)]
            except:
                raise ValueError("palauta metodiin annettava kohde on oltava (x,y) tuple tai indeksi kokonaisluku")


    def aseta(self, xy: tuple, arvo: list):
        try:
            self.r[int(xy[1])*self.leveys + int(xy[0])] = arvo
        except:
            try:
                self.r[int(xy)] = arvo
            except:
                raise ValueError("Aseta metodiin annettava kohde on oltava (x,y) tuple tai indeksi kokonaisluku")

    def koord(self, indeksi: int):
        return (indeksi % self.leveys, indeksi // self.leveys)

    def naapurit(self, xy: tuple):
        
        naapurit = []
        try:
            x, y = xy
            if x > 0:
                naapurit.append((x-1, y))
            if x < self.leveys-1:
                naapurit.append((x+1, y))
            if y > 0:
                naapurit.append((x, y-1))
            if y < self.korkeus-1:
                naapurit.append((x, y+1))
            return naapurit
        except:
            try:
                indeksi = xy
                x, y = self.koord(indeksi)
                if x > 0:
                    naapurit.append((x-1, y))
                if x < self.leveys-1:
                    naapurit.append((x+1, y))
                if y > 0:
                    naapurit.append((x, y-1))
                if y < self.korkeus-1:
                    naapurit.append((x, y+1))
                return naapurit
            except:
                raise ValueError("Naapurit metodiin annettava kohde on oltava (x,y) tuple tai indeksi kokonaisluku")
            


class Ruutu:
    def __init__(self, osa: int):
        self.osa = osa
        self.yla = []
        self.ala = []
        self.vasen = []
        self.oikea = []


    def __str__(self):
        return str(self.osa)
leveys = 5
korkeus = 5
palikat = []
for i in range(9):
    rr = Ruutu(i)
    palikat.append(rr)
r = []
r.append([0,1,1,0])
r.append([0,1,1,1])
r.append([0,0,1,1])
r.append([1,1,1,0])
r.append([0,0,0,0])
r.append([1,0,1,1])
r.append([1,1,0,0])
r.append([1,1,0,1])
r.append([1,0,0,1])

for i in range(9):
    yla = []
    oikea = []
    ala = []
    vasen = []
    for j in range(9):
        if r[i][0] == r[j][2]:
            yla.append(j)
        if r[i][1] == r[j][3]:
            oikea.append(j)
        if r[i][2] == r[j][0]:
            ala.append(j)
        if r[i][3] == r[j][1]:
            vasen.append(j)
    print(i, yla, oikea, ala, vasen)
    palikat[i].yla = yla
    palikat[i].ala = ala
    palikat[i].vasen = vasen
    palikat[i].oikea = oikea
        
kuva = Ruudukko(5, 5, 9)
