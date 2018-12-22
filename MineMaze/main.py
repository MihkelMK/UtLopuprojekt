import pygame as pg
import random
import pickle
import sys
from os import path
from settings import *
from classes import *
from tilemap import *


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.init()
pg.mixer.init()

#Pildisisestamised
küsi_väljumist = pg.image.load("sprites/menus/doyouwanttoexit.png")
menüü = pg.image.load("sprites/menus/mainmenu.png")
tiitrid = pg.image.load("sprites/menus/Credits.png")
spraidid = pg.image.load("sprites/menus/chooseasprite.png")
läbi = pg.image.load("sprites/menus/gameover.png")
skoor = pg.image.load("sprites/menus/scoreboard.png")
tiitrid_close = pg.image.load("sprites/menus/Buttons/CloseCredits.png")
sprite_choose = pg.image.load("sprites/menus/Buttons/Choose.png")
sprite_chosen = pg.image.load("sprites/menus/Buttons/Chosen.png")
quityes = pg.image.load("sprites/menus/Buttons/QuitYes.png")
quitno = pg.image.load("sprites/menus/Buttons/QuitNo.png")
play_yes = pg.image.load("sprites/menus/Buttons/Play.png")
play_no = pg.image.load("sprites/menus/Buttons/NoPlay.png")
save_yes = pg.image.load("sprites/menus/Buttons/YesSave.png")
save_no = pg.image.load("sprites/menus/Buttons/NoSave.png")
scorecloser = pg.image.load("sprites/menus/Buttons/CloseScoreboard.png")
import_players()
#test
font = pg.font.Font(None, 100)
menüüs = font.render("Start", 1, [255, 255, 255])
menüüson = font.render("Start", 1, [212, 129, 0])
#lõpp
mäng_töötab = True
mängu_etapp = "menüü"
choice = 0
valik = 0
nimi = ''
nameerror = 0
start = False
tabeli_y = 44
scoremax = 8
score_place = None

#Skooritabeli jaoks:
try:
    fail = open('highscore.pickle','rb')
    scoreboard = pickle.load(fail)
    fail.close()
except:
    scoreboard = []

while mäng_töötab:
    while mängu_etapp == "menüü":
        hiire_x, hiire_y = pg.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                mängu_etapp = "quit"
                meelde = "menüü"
                choice = 0
            if i.type == pg.KEYUP:
                if i.key == pg.K_UP:
                    if choice == 1 or choice == 0:
                        choice = 5
                    if choice == 3:
                        choice = 1
                    else:
                        choice = choice - 1
                if i.key == pg.K_DOWN:
                    if choice == 5 or choice == 0:
                        choice = 1
                    if choice == 1:
                        choice = 3
                    else:
                        choice = choice + 1
                if i.key == pg.K_RETURN:
                    if choice == 1:
                        mängu_etapp = "sprite"
                        choice = 0
                    elif choice == 3:
                        mängu_etapp = "scoreboard"
                        choice = 0
                    elif choice == 4:
                        mängu_etapp = "tiitrid"
                    elif choice == 5:
                        #Kui Quit on oranž, läheb mäng kinni.
                        mäng_töötab = False
                        break
            if i.type == pg.MOUSEBUTTONUP:
                if hiire_x > 312 and hiire_x < 662 and hiire_y > 394 and hiire_y < 480:
                    mängu_etapp = "sprite"
                if hiire_x > 312 and hiire_x < 662 and hiire_y > 574 and hiire_y < 668:
                    mängu_etapp = "scoreboard"
                if hiire_x > 312 and hiire_x < 662 and hiire_y > 668 and hiire_y < 762:
                    mängu_etapp = "tiitrid"
                #pg.mouse button up tähendab, et kas vasaku või parema klahvi vajutamisel ja üles tõstmisel nupp aktiveerub. Hiirerull ka töötab!
                if hiire_x > 312 and hiire_x < 662 and hiire_y > 762 and hiire_y < 856:
                    #Kui vajutada Quit nuppu, mäng sulgub.
                    mäng_töötab = False
                    break
                else:
                    choice = 0
        screen.fill([0, 0, 0])
        screen.blit(menüü, [0, 0])
        #Kiri kirjutatakse nii: kui selle peale ei osutata, on see valge. Kui selle peale osutatakse, muutub see oranžiks ja selle peale vajutades juhtub midagi.
        #Kõik see on konstrueeritud selle alusel, et kõik kirjad jagavad ühte ja sama osutuskaugust x-teljel ja y-teljel suureneb osutus kaugus iga kord 94 võrra.
        if hiire_x > 312 and hiire_x < 662 and hiire_y > 394 and hiire_y < 480 or choice == 1:
            screen.blit(menüüson, [410, 400])
        else:
            screen.blit(menüüs, [410, 400])
        if hiire_x > 312 and hiire_x < 662 and hiire_y > 574 and hiire_y < 668 or choice == 3:
            screen.blit(font.render("Highscore", 1, [212, 129, 0]), [322, 580])
        else:
            screen.blit(font.render("Highscore", 1, [255, 255, 255]), [322, 580])
        if hiire_x > 312 and hiire_x < 662 and hiire_y > 668 and hiire_y < 762 or choice == 4:
            screen.blit(font.render("Credits", 1, [212, 129, 0]), [360, 670])
        else:
            screen.blit(font.render("Credits", 1, [255, 255, 255]), [360, 670])
        if hiire_x > 312 and hiire_x < 662 and hiire_y > 762 and hiire_y < 856 or choice == 5:
            screen.blit(font.render("Quit", 1, [255, 98, 38]), [410, 760])
        else:
            screen.blit(font.render("Quit", 1, [255, 255, 255]), [410, 760])
        pg.display.flip()
        pg.time.delay(1)
        #
        #Et olla ikka kindel, et mäng sulgub.
        if mäng_töötab == False:
            break
        
    while mängu_etapp == "tiitrid":
        #Siin tuleb ainult kuvada pilt ja ära määrata klikkimiskaugus.
        hiire_x, hiire_y = pg.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                mängu_etapp = "quit"
                meelde = "tiitrid"
                choice = 0
            if i.type == pg.KEYUP:
                if i.key == pg.K_RETURN:
                    mängu_etapp = "menüü"
            if i.type == pg.MOUSEBUTTONUP:
                if hiire_x > 395 and hiire_x < 607 and hiire_y > 863 and hiire_y < 973:
                    mängu_etapp = "menüü"
        screen.blit(tiitrid, [0, 0])
        if hiire_x > 395 and hiire_x < 607 and hiire_y > 863 and hiire_y < 973:
            screen.blit(tiitrid_close, [395, 863])
        pg.display.flip()
        
    while mängu_etapp == "sprite":
        hiire_x, hiire_y = pg.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.KEYUP:
                if i.key == pg.K_RIGHT:
                    if choice == 0:
                        choice = 1
                    elif choice == 9:
                        choice = 1
                    else:
                        choice = choice + 1
                if i.key == pg.K_LEFT:
                    if choice == 0:
                        choice = 9
                    elif choice == 1:
                        choice = 9
                    else:
                        choice = choice - 1
                if i.key == pg._RETURN:
                    if choice == 0:
                        choice = 1
                    mängu_etapp = "mängijadefineerimine"
            if i.type == pg.MOUSEBUTTONUP:
                if hiire_x > 51 and hiire_x < 149 and hiire_y > 698 and hiire_y < 799:
                    choice = 1
                if hiire_x > 149 and hiire_x < 247 and hiire_y > 698 and hiire_y < 799:
                    choice = 2
                if hiire_x > 247 and hiire_x < 345 and hiire_y > 698 and hiire_y < 799:
                    choice = 3
                if hiire_x > 345 and hiire_x < 443 and hiire_y > 698 and hiire_y < 799:
                    choice = 4
                if hiire_x > 443 and hiire_x < 541 and hiire_y > 698 and hiire_y < 799:
                    choice = 5
                if hiire_x > 541 and hiire_x < 639 and hiire_y > 698 and hiire_y < 799:
                    choice = 6
                if hiire_x > 639 and hiire_x < 737 and hiire_y > 698 and hiire_y < 799:
                    choice = 7
                if hiire_x > 737 and hiire_x < 835 and hiire_y > 698 and hiire_y < 799:
                    choice = 8
                if hiire_x > 835 and hiire_x < 933 and hiire_y > 698 and hiire_y < 799:
                    choice = 9
                if hiire_x > 21 and hiire_x < 179 and hiire_y > 21 and hiire_y < 104:
                    choice = 0
                    mängu_etapp = "menüü"
                if hiire_x > 373 and hiire_x < 612 and hiire_y > 851 and hiire_y < 972:
                    if choice == 0:
                        choice = 1
                    mängu_etapp = "mängijadefineerimine"
            if i.type == pg.QUIT:
                mängu_etapp = "quit"
                meelde = "sprite"
                choice = 0
        screen.blit(spraidid, [0, 0])
        if choice == 1:
            screen.blit(sprite_chosen, [51, 698])
        if choice == 2:
            screen.blit(sprite_chosen, [149, 698])
        if choice == 3:
            screen.blit(sprite_chosen, [247, 698])
        if choice == 4:
            screen.blit(sprite_chosen, [345, 698])
        if choice == 5:
            screen.blit(sprite_chosen, [443, 698])
        if choice == 6:
            screen.blit(sprite_chosen, [541, 698])
        if choice == 7:
            screen.blit(sprite_chosen, [639, 698])
        if choice == 8:
            screen.blit(sprite_chosen, [737, 698])
        if choice == 9:
            screen.blit(sprite_chosen, [835, 698])
        if hiire_x > 51 and hiire_x < 149 and hiire_y > 698 and hiire_y < 799 and choice != 1:
            screen.blit(sprite_choose, [51, 698])
        if hiire_x > 149 and hiire_x < 247 and hiire_y > 698 and hiire_y < 799 and choice != 2:
            screen.blit(sprite_choose, [149, 698])
        if hiire_x > 247 and hiire_x < 345 and hiire_y > 698 and hiire_y < 799 and choice != 3:
            screen.blit(sprite_choose, [247, 698])
        if hiire_x > 345 and hiire_x < 443 and hiire_y > 698 and hiire_y < 799 and choice != 4:
            screen.blit(sprite_choose, [345, 698])
        if hiire_x > 443 and hiire_x < 541 and hiire_y > 698 and hiire_y < 799 and choice != 5:
            screen.blit(sprite_choose, [443, 698])
        if hiire_x > 541 and hiire_x < 639 and hiire_y > 698 and hiire_y < 799 and choice != 6:
            screen.blit(sprite_choose, [541, 698])
        if hiire_x > 639 and hiire_x < 737 and hiire_y > 698 and hiire_y < 799 and choice != 7:
            screen.blit(sprite_choose, [639, 698])
        if hiire_x > 737 and hiire_x < 835 and hiire_y > 698 and hiire_y < 799 and choice != 8:
            screen.blit(sprite_choose, [737, 698])
        if hiire_x > 835 and hiire_x < 933 and hiire_y > 698 and hiire_y < 799 and choice != 9:
            screen.blit(sprite_choose, [835, 698])
        if hiire_x > 373 and hiire_x < 612 and hiire_y > 851 and hiire_y < 972:
            screen.blit(play_yes, [373, 851])
        if hiire_x > 21 and hiire_x < 179 and hiire_y > 21 and hiire_y < 104:
            screen.blit(play_no, [21, 21])
        pg.display.flip()
        pg.time.delay(5)
    
    while mängu_etapp == "mängijadefineerimine":
        if choice == 1:
            player = pg.image.load("sprites/game/white.png")
            start = True
        if choice == 2:
            player = pg.image.load("sprites/game/blue.png")
            start = True
        if choice == 3:
            player = pg.image.load("sprites/game/pink.png")
            start = True
        if choice == 4:
            player = pg.image.load("sprites/game/gray.png")
            start = True
        if choice == 5:
            player = pg.image.load("sprites/game/green.png")
            start = True
        if choice == 6:
            player = pg.image.load("sprites/game/yellow.png")
            start = True
        if choice == 7:
            player = pg.image.load("sprites/game/purple.png")
            start = True
        if choice == 8:
            player = pg.image.load("sprites/game/rose.png")
            start = True
        if choice == 9:
            choice = random.randint(1,8)
        if start:
            mängu_etapp = "mäng"
  
#########
    while mängu_etapp == "mäng":
        def draw_player_health(surf, x, y, pct):
            if pct < 0:
                pct = 0
            BAR_LENGTH = 100
            BAR_HEIGHT = 20
            fill = pct * BAR_LENGTH
            outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
            fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
            if pct > 0.6:
                col = GREEN
            elif pct > 0.3:
                col = YELLOW
            else:
                col = RED
            pg.draw.rect(surf, col, fill_rect)
            pg.draw.rect(surf, WHITE, outline_rect, 2)

        class Game:
            def __init__(self):
                pg.init()
                self.screen = pg.display.set_mode((WIDTH, HEIGHT))
                pg.display.set_caption(TITLE)
                self.clock = pg.time.Clock()
                self.load_data()

            def load_data(self):
                game_folder = path.dirname("__file__")
                img_folder = path.join(game_folder, "sprites/game")
                pg.mixer.music.load(path.join(game_folder, "taust.mp3"))
                self.map = Map(path.join(game_folder, "map.txt"))
                self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
                self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
                self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
                self.stone_img = pg.image.load(path.join(img_folder, STONE_IMG)).convert_alpha()

            def new(self):
                # initialize all variables and do all the setup for a new game
                self.all_sprites = pg.sprite.Group()
                self.walls = pg.sprite.Group()
                self.mobs = pg.sprite.Group()
                self.bullets = pg.sprite.Group()
                self.stones = pg.sprite.Group()
                self.spawners = pg.sprite.Group()
                for row, tiles in enumerate(self.map.data):
                    for col, tile in enumerate(tiles):
                        if tile == 'W':
                            Wall(self, col, row)
                        if tile == 'I':
                            Stone(self, col, row)
                        if tile == 'S':
                            self.spawner = Spawner(self, col, row)
                        if tile == 'P':
                            self.player = Player(self, col, row)
                self.camera = Camera(self.map.width, self.map.height)
                pg.mixer.music.play(-1, 0)

            def run(self):
                # game loop - set self.playing = False to end the game
                self.playing = True
                while self.playing:
                    self.dt = self.clock.tick(FPS) / 1000
                    self.events()
                    self.update()
                    self.draw()

            def quit(self):
                mängu_etapp == "game_over"

            def update(self):
                # update portion of the game loop
                self.all_sprites.update()
                self.camera.update(self.player)
                
                hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
                for hit in hits:
                    self.player.health -= MOB_DAMAGE
                    hit.vel = vec(0, 0)
                    if self.player.health <= 0:
                        self.playing = False
                        self.quit()
                if hits:
                    self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
                    
                hits = pg.sprite.groupcollide(self.mobs, self.bullets, True, True)
                
                hits = pg.sprite.spritecollide(self.player, self.stones, False)
                for hit in hits:
                    if hit and self.player.ammo < PLAYER_MAX_AMMO:
                        self.player.ammo += 1
                        hit.kill()
                    else:
                        return
                    
                hits = pg.sprite.spritecollide(self.player, self.spawners, True, collide_hit_rect)
                for hit in hits:
                    Mob(self, hit.x, hit.y)
                    print(hit.rect)
                    hit.kill()   
                
            def draw(self):
                pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
                self.screen.fill(BGCOLOR)
                for sprite in self.all_sprites:
                    self.screen.blit(sprite.image, self.camera.apply(sprite))
                draw_player_health(self.screen, 8, 10, self.player.health / PLAYER_HEALTH)
                
                self.player.draw_ammo(10, 30, self.screen, 25)
                pg.display.flip()
            
            def events(self):
                # catch all events here
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.quit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.quit()

        g = Game()
        g.new()
        g.run()


        punktid_kivi = random.randint(0,1000)
        punktid_miin = random.randint(0,1000)
        punktid_aeg = random.randint(0,1000)
        punktid_kokku = punktid_kivi + punktid_miin + punktid_aeg
        mängu_etapp = "game_over"
#########     
    while mängu_etapp == "game_over":
        hiire_x, hiire_y = pg.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.KEYUP:
                if i.key == pg.K_RETURN:
                    if nimi == '':
                        nameerror = 1
                    else:
                        nameerror = 0
                        mängu_etapp = "salvestamine"
                if i.key == pg.K_BACKSPACE:
                    nimi = nimi[:-1]
                elif i.key <= 127:
                    if pg.key.get_mods() & pg.KMOD_SHIFT:
                        nimi += chr(i.key).upper()
                    else:
                        nimi += chr(i.key)
                    if len(nimi) >= 11:
                        nimi = nimi[:-1]
            if i.type == pg.MOUSEBUTTONUP:
                if hiire_x > 553 and hiire_x < 753 and hiire_y > 900 and hiire_y < 991:
                    if nimi == '':
                        nameerror = 1
                    else:
                        nameerror = 0
                        mängu_etapp = "salvestamine"
                if hiire_x > 264 and hiire_x < 501 and hiire_y > 900 and hiire_y < 991:
                    choice = 0
                    mängu_etapp = "menüü"
            if i.type == pg.QUIT:
                mängu_etapp = "quit"
                meelde = "game_over"
                choice = 0
        screen.blit(läbi, [0, 0])
        screen.blit(font.render(str(punktid_kivi), 1, [255, 255, 255]), [542, 309])
        screen.blit(font.render(str(punktid_miin), 1, [255, 255, 255]), [542, 399])
        screen.blit(font.render(str(punktid_aeg), 1, [255, 255, 255]), [542, 485])
        screen.blit(font.render(str(punktid_kokku), 1, [255, 255, 255]), [542, 575])
        screen.blit(font.render(nimi, 1, [255, 255, 255]), [276, 798])
        if hiire_x > 553 and hiire_x < 753 and hiire_y > 900 and hiire_y < 991:
            screen.blit(save_yes, [553, 900])
        if hiire_x > 264 and hiire_x < 501 and hiire_y > 900 and hiire_y < 991:
            screen.blit(save_no, [264, 900])
        if nameerror == 1:
            screen.blit(font.render("You must enter your name!", 1, [255, 0, 0]), [50, 710])
        pg.display.flip()
        
    while mängu_etapp == "salvestamine":
        scoreboard = scoreboard[:scoremax]
        scoreboard.append((punktid_kokku, nimi))
        scoreboard.sort(reverse=True)
        fail = open('highscore.pickle', 'wb')
        pickle.dump(scoreboard,fail)
        mängu_etapp = "scoreboard"
        
    while mängu_etapp == "scoreboard":
        hiire_x, hiire_y = pg.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.KEYUP:
                if i.key == pg.K_RETURN:
                    choice = 0
                    mängu_etapp = "menüü"
            if i.type == pg.MOUSEBUTTONUP:
                if hiire_x > 400 and hiire_x < 599 and hiire_y > 928 and hiire_y < 994:
                    choice = 0
                    mängu_etapp = "menüü"
            if i.type == pg.QUIT:
                mängu_etapp = "quit"
                meelde = "scoreboard"
                choice = 0
        screen.blit(skoor, [0, 0])
        for t in range(len(scoreboard)):
            (punktid_kokku, nimi) = scoreboard[t]
            tabeli_y = tabeli_y + 99
            screen.blit(font.render(nimi, 1, [255, 255, 255]), [137, tabeli_y])
            screen.blit(font.render(str(punktid_kokku), 1, [255, 255, 255]), [610, tabeli_y])
        tabeli_y = 44
        if hiire_x > 400 and hiire_x < 599 and hiire_y > 928 and hiire_y < 994:
            screen.blit(scorecloser, [400, 928])
        pg.display.flip()

    while mängu_etapp == "quit":
        hiire_x, hiire_y = pg.mouse.get_pos()
        for i in pg.event.get():
            if i.type == pg.KEYUP:
                #Siin ma defineerin nooltega navigeerimist. Choice 1 on No, Choice 2 on Yes.
                if i.key == pg.K_RIGHT:
                    if choice == 0:
                        choice = 2
                    elif choice == 1:
                        choice = 2
                    elif choice == 2:
                        choice = 1
                if i.key == pg.K_LEFT:
                    if choice == 0:
                        choice = 1
                    elif choice == 1:
                        choice = 2
                    elif choice == 2:
                        choice = 1
                if i.key == pg.K_RETURN:
                    #Kui on No (Choice 1), mäng jätkub, kuid kui on Yes (Choice 2), mäng sulgub.
                    if choice == 1:
                        choice = 0
                        mängu_etapp = meelde
                    elif choice == 2:
                        mängu_etapp = 0
                        if meelde == "mäng":
                            mängu_etapp = "game_over"
                        else:
                            mäng_töötab = False
                            break
            if i.type == pg.MOUSEBUTTONUP:
                if hiire_x > 312 and hiire_x < 460 and hiire_y > 504 and hiire_y < 617:
                    #Kui vajutada No, siis mäng jätkub.
                    mängu_etapp = meelde
                if hiire_x > 540 and hiire_x < 688 and hiire_y > 504 and hiire_y < 617:
                    #Kui vajutada Yes, siis mäng sulgub.
                    if meelde == "mäng":
                        mängu_etapp = "game_over"
                    else:
                        mäng_töötab = False
                        break
                else:
                    #Muidu tühista nooleklahvidega tehtud valik.
                    choice = 0
            if i.type == pg.QUIT:
                if meelde == "mäng":
                    mängu_etapp = "game_over"
                else:
                    mängu_etapp = 0
                    mäng_töötab = False
                    break
        #Tekita väljumist küsiv paneel ja peata mäng.
        screen.blit(küsi_väljumist, [250, 250])
        #Kui hiirega osutatakse või nooleklahviga navigeeritakse, siis see valik muutub oranžiks.
        if hiire_x > 312 and hiire_x < 460 and hiire_y > 504 and hiire_y < 617:
            screen.blit(quitno, [312, 504])
        if choice == 1:
            screen.blit(quitno, [312, 504])
        if hiire_x > 540 and hiire_x < 688 and hiire_y > 504 and hiire_y < 617:
            screen.blit(quityes, [540, 504])
        if choice == 2:
            screen.blit(quityes, [540, 504])
        pg.display.flip()
        if mäng_töötab == False:
            #Kui mäng sulgub, siis see ikka suletakse.
            break

quit()