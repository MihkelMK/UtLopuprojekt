from classes.player import *
from settings import *
# Impordime sätted ja kõik klassid

# Teeme akna ja defineerime juba clock'i,
# nii on tulevikus kompaktsem kood
window = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()

# Teene spraidi grupi, kuhu kuuluvad kõik spraidi
# ja paneme mängia sinna sisse.
sprites = pg.sprite.Group()
player = Player()
sprites.add(player)

# Põhitsükkel
running = True
while running:
    # Kui mäng pannakse kinni, siis lõpeta tsükkel.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Kasutane kõikide spraitide põhi funktsiooni.
    sprites.update()
    
    # Täidame tausta värviga "BACKGROUND",
    # joonistame kõik spraidid ja kuvame selle monitile.
    window.fill(BACKGROUND)
    sprites.draw(window)
    pg.display.flip()

sys.exit()
pg.quit()