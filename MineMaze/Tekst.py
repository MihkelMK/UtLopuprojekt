from pygame import *

aken = display.set_mode([1024, 1000])
init()

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
    white = image.load("Mängija/white.png")
    blue = image.load("Mängija/blue.png")
    pink = image.load("Mängija/pink.png")
    gray = image.load("Mängija/gray.png")
    green = image.load("Mängija/green.png")
    yellow = image.load("Mängija/yellow.png")
    purple = image.load("Mängija/purple.png")
    rose = image.load("Mängija/rose.png")
    custom = image.load("Mängija/custom.png")
    
    
def menüü(ekraan):
    ekraan.fill([0, 0, 0])
    ekraan.blit(menüü, [0, 0])
    display.flip()
    time.delay(50)

    
