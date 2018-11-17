import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
# See jama on vajalik, et saaksin eelmisest kaustast setting.py importida.
# Kui on mingi parem viis, siis muutke ära.

# Impordin sätted
from settings import *

# Klass mängia, sprite.
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Ülteme, et mängia on 50x50 ruut enne defineeritud värvi "PLAYER"
        self.image = pg.Surface((50, 50))
        self.image.fill(PLAYER)
        # Saame mängia suuruse ekraanil
        self.rect = self.image.get_rect()
        # Üteleme, kuhu mängia tekib mängu alguses
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 40
        # Pneme kiirused nulli alguses
        self.speedx = 0
        self.speedy = 0
        
    # Põhi tsükklisse minev funktsioon
    def update(self):
        # Paneme kiirused nulli
        self.speedx = 0
        self.speedy = 0
        # Liikumis mehhanism. Kui nuppu vajutatakse, muudame kiirust.
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            self.speedx = 8
        if key[pg.K_LEFT]:
            self.speedx = -8
        if key[pg.K_UP]:
            self.speedy = -8
        if key[pg.K_DOWN]:
            self.speedy = 8
        # Muudame kiiruse väärtuses mängia asukohta.
        self.rect.x += self.speedx  
        self.rect.y += self.speedy
        
        # Hoiame mängiat ekraani piirides.
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        elif self.rect.top < 0:
            self.rect.top = 0