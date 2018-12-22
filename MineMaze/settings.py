import pygame as pg

# define some colors (R, G, B)
PLAYER = (120, 190, 200)
ENEMY = (245, 90, 60)
BACKGROUND = (210, 210, 210)
WALL = (130, 130, 130)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# game settings
WIDTH = 1000   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 1000  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "MineMaze"
BGCOLOR = BACKGROUND

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250.0
PLAYER_IMG = "white.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 40, 40)
PLAYER_HEALTH = 100
PLAYER_AMMO = 10
PLAYER_MAX_AMMO = 15

# Mob settings
MOB_IMG = "enemy.png"
MOB_SPEED = 700
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20

# Gun settings
BULLET_IMG = "stone.png"
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 400
KICKBACK = 200
GUN_SPREAD = 5

# Items
STONE_IMG = "stone.png"

# Spawner settings
SPAWNER_HIT_RECT = pg.Rect(0, 0, 200, 200)




### Menu globals and settings ###

def import_text():
    global font
    font = font.Font(None, 50)
    global menüüs
    menüüs = font.render("Start", 1, [255, 255, 255])
    global menüüson
    menüüson = font.render("Start", 1, [212, 129, 0])
    global menüüv
    menüüv = font.render("Valikud", 1, [255, 255, 255])
    global menüüvon
    menüüvon = font.render("Valikud", 1, [212, 129, 0])

def import_players():
    global white
    global blue
    global pink
    global gray
    global green
    global yellow
    global purple
    global rose
    global custom
    white = pg.image.load("sprites/game/white.png")
    blue = pg.image.load("sprites/game/blue.png")
    pink = pg.image.load("sprites/game/pink.png")
    gray = pg.image.load("sprites/game/gray.png")
    green = pg.image.load("sprites/game/green.png")
    yellow = pg.image.load("sprites/game/yellow.png")
    purple = pg.image.load("sprites/game/purple.png")
    rose = pg.image.load("sprites/game/rose.png")
    custom = pg.image.load("sprites/game/custom.png")
    
    
def menüü(ekraan):
    ekraan.fill([0, 0, 0])
    ekraan.blit(menüü, [0, 0])
    display.flip()
    time.delay(50)