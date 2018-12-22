import random
import pickle
from Tekst import *

#Pildisisestamised
küsi_väljumist = image.load("doyouwanttoexit.png")
menüü = image.load("mainmenu.png")
tiitrid = image.load("Credits.png")
spraidid = image.load("chooseasprite.png")
läbi = image.load("gameover.png")
skoor = image.load("scoreboard.png")
tiitrid_close = image.load("Buttons/CloseCredits.png")
sprite_choose = image.load("Buttons/Choose.png")
sprite_chosen = image.load("Buttons/Chosen.png")
quityes = image.load("Buttons/QuitYes.png")
quitno = image.load("Buttons/QuitNo.png")
play_yes = image.load("Buttons/Play.png")
play_no = image.load("Buttons/NoPlay.png")
save_yes = image.load("Buttons/YesSave.png")
save_no = image.load("Buttons/NoSave.png")
scorecloser = image.load("Buttons/CloseScoreboard.png")
import_players()
#test
font = font.Font(None, 100)
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
        hiire_x, hiire_y = mouse.get_pos()
        for i in event.get():
            if i.type == QUIT:
                mängu_etapp = "quit"
                meelde = "menüü"
                choice = 0
            if i.type == KEYUP:
                if i.key == K_UP:
                    if choice == 1 or choice == 0:
                        choice = 5
                    if choice == 3:
                        choice = 1
                    else:
                        choice = choice - 1
                if i.key == K_DOWN:
                    if choice == 5 or choice == 0:
                        choice = 1
                    if choice == 1:
                        choice = 3
                    else:
                        choice = choice + 1
                if i.key == K_RETURN:
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
            if i.type == MOUSEBUTTONUP:
                if hiire_x > 324 and hiire_x < 674 and hiire_y > 394 and hiire_y < 480:
                    mängu_etapp = "sprite"
                if hiire_x > 324 and hiire_x < 674 and hiire_y > 574 and hiire_y < 668:
                    mängu_etapp = "scoreboard"
                if hiire_x > 324 and hiire_x < 674 and hiire_y > 668 and hiire_y < 762:
                    mängu_etapp = "tiitrid"
                #Mouse button up tähendab, et kas vasaku või parema klahvi vajutamisel ja üles tõstmisel nupp aktiveerub. Hiirerull ka töötab!
                if hiire_x > 324 and hiire_x < 674 and hiire_y > 762 and hiire_y < 856:
                    #Kui vajutada Quit nuppu, mäng sulgub.
                    mäng_töötab = False
                    break
                else:
                    choice = 0
        aken.fill([0, 0, 0])
        aken.blit(menüü, [12, 0])
        #Kiri kirjutatakse nii: kui selle peale ei osutata, on see valge. Kui selle peale osutatakse, muutub see oranžiks ja selle peale vajutades juhtub midagi.
        #Kõik see on konstrueeritud selle alusel, et kõik kirjad jagavad ühte ja sama osutuskaugust x-teljel ja y-teljel suureneb osutus kaugus iga kord 94 võrra.
        if hiire_x > 324 and hiire_x < 674 and hiire_y > 394 and hiire_y < 480 or choice == 1:
            aken.blit(menüüson, [422, 400])
        else:
            aken.blit(menüüs, [422, 400])
        if hiire_x > 324 and hiire_x < 674 and hiire_y > 574 and hiire_y < 668 or choice == 3:
            aken.blit(font.render("Highscore", 1, [212, 129, 0]), [334, 580])
        else:
            aken.blit(font.render("Highscore", 1, [255, 255, 255]), [334, 580])
        if hiire_x > 324 and hiire_x < 674 and hiire_y > 668 and hiire_y < 762 or choice == 4:
            aken.blit(font.render("Credits", 1, [212, 129, 0]), [372, 670])
        else:
            aken.blit(font.render("Credits", 1, [255, 255, 255]), [372, 670])
        if hiire_x > 324 and hiire_x < 674 and hiire_y > 762 and hiire_y < 856 or choice == 5:
            aken.blit(font.render("Quit", 1, [255, 98, 38]), [422, 760])
        else:
            aken.blit(font.render("Quit", 1, [255, 255, 255]), [422, 760])
        display.flip()
        time.delay(1)
        #
        #Et olla ikka kindel, et mäng sulgub.
        if mäng_töötab == False:
            break
        
    while mängu_etapp == "tiitrid":
        hiire_x, hiire_y = mouse.get_pos()
        for i in event.get():
            if i.type == QUIT:
                mängu_etapp = "quit"
                meelde = "tiitrid"
                choice = 0
            if i.type == KEYUP:
                if i.key == K_RETURN:
                    mängu_etapp = "menüü"
            if i.type == MOUSEBUTTONUP:
                if hiire_x > 407 and hiire_x < 619 and hiire_y > 863 and hiire_y < 973:
                    mängu_etapp = "menüü"
        aken.blit(tiitrid, [0, 0])
        if hiire_x > 407 and hiire_x < 619 and hiire_y > 863 and hiire_y < 973:
            aken.blit(tiitrid_close, [407, 863])
        display.flip()
        
    while mängu_etapp == "sprite":
        hiire_x, hiire_y = mouse.get_pos()
        for i in event.get():
            if i.type == KEYUP:
                if i.key == K_RIGHT:
                    if choice == 0:
                        choice = 1
                    elif choice == 9:
                        choice = 1
                    else:
                        choice = choice + 1
                if i.key == K_LEFT:
                    if choice == 0:
                        choice = 9
                    elif choice == 1:
                        choice = 9
                    else:
                        choice = choice - 1
                if i.key == K_RETURN:
                    if choice == 0:
                        choice = 1
                    mängu_etapp = "mängijadefineerimine"
            if i.type == MOUSEBUTTONUP:
                if hiire_x > 63 and hiire_x < 161 and hiire_y > 698 and hiire_y < 799:
                    choice = 1
                if hiire_x > 161 and hiire_x < 259 and hiire_y > 698 and hiire_y < 799:
                    choice = 2
                if hiire_x > 259 and hiire_x < 357 and hiire_y > 698 and hiire_y < 799:
                    choice = 3
                if hiire_x > 357 and hiire_x < 455 and hiire_y > 698 and hiire_y < 799:
                    choice = 4
                if hiire_x > 455 and hiire_x < 553 and hiire_y > 698 and hiire_y < 799:
                    choice = 5
                if hiire_x > 553 and hiire_x < 651 and hiire_y > 698 and hiire_y < 799:
                    choice = 6
                if hiire_x > 651 and hiire_x < 749 and hiire_y > 698 and hiire_y < 799:
                    choice = 7
                if hiire_x > 749 and hiire_x < 847 and hiire_y > 698 and hiire_y < 799:
                    choice = 8
                if hiire_x > 847 and hiire_x < 945 and hiire_y > 698 and hiire_y < 799:
                    choice = 9
                if hiire_x > 33 and hiire_x < 191 and hiire_y > 21 and hiire_y < 104:
                    choice = 0
                    mängu_etapp = "menüü"
                if hiire_x > 385 and hiire_x < 624 and hiire_y > 851 and hiire_y < 972:
                    if choice == 0:
                        choice = 1
                    mängu_etapp = "mängijadefineerimine"
            if i.type == QUIT:
                mängu_etapp = "quit"
                meelde = "sprite"
                choice = 0
        aken.blit(spraidid, [12, 0])
        if choice == 1:
            aken.blit(sprite_chosen, [63, 698])
        if choice == 2:
            aken.blit(sprite_chosen, [161, 698])
        if choice == 3:
            aken.blit(sprite_chosen, [259, 698])
        if choice == 4:
            aken.blit(sprite_chosen, [357, 698])
        if choice == 5:
            aken.blit(sprite_chosen, [455, 698])
        if choice == 6:
            aken.blit(sprite_chosen, [553, 698])
        if choice == 7:
            aken.blit(sprite_chosen, [651, 698])
        if choice == 8:
            aken.blit(sprite_chosen, [749, 698])
        if choice == 9:
            aken.blit(sprite_chosen, [847, 698])
        if hiire_x > 63 and hiire_x < 161 and hiire_y > 698 and hiire_y < 799 and choice != 1:
            aken.blit(sprite_choose, [63, 698])
        if hiire_x > 161 and hiire_x < 259 and hiire_y > 698 and hiire_y < 799 and choice != 2:
            aken.blit(sprite_choose, [161, 698])
        if hiire_x > 259 and hiire_x < 357 and hiire_y > 698 and hiire_y < 799 and choice != 3:
            aken.blit(sprite_choose, [259, 698])
        if hiire_x > 357 and hiire_x < 455 and hiire_y > 698 and hiire_y < 799 and choice != 4:
            aken.blit(sprite_choose, [357, 698])
        if hiire_x > 455 and hiire_x < 553 and hiire_y > 698 and hiire_y < 799 and choice != 5:
            aken.blit(sprite_choose, [455, 698])
        if hiire_x > 553 and hiire_x < 651 and hiire_y > 698 and hiire_y < 799 and choice != 6:
            aken.blit(sprite_choose, [553, 698])
        if hiire_x > 651 and hiire_x < 749 and hiire_y > 698 and hiire_y < 799 and choice != 7:
            aken.blit(sprite_choose, [651, 698])
        if hiire_x > 749 and hiire_x < 847 and hiire_y > 698 and hiire_y < 799 and choice != 8:
            aken.blit(sprite_choose, [749, 698])
        if hiire_x > 847 and hiire_x < 945 and hiire_y > 698 and hiire_y < 799 and choice != 9:
            aken.blit(sprite_choose, [847, 698])
        if hiire_x > 385 and hiire_x < 624 and hiire_y > 851 and hiire_y < 972:
            aken.blit(play_yes, [385, 851])
        if hiire_x > 33 and hiire_x < 191 and hiire_y > 21 and hiire_y < 104:
            aken.blit(play_no, [33, 21])
        display.flip()
        time.delay(5)
    
    while mängu_etapp == "mängijadefineerimine":
        if choice == 1:
            player = image.load("Mängija/white.png")
            start = True
        if choice == 2:
            player = image.load("Mängija/blue.png")
            start = True
        if choice == 3:
            player = image.load("Mängija/pink.png")
            start = True
        if choice == 4:
            player = image.load("Mängija/gray.png")
            start = True
        if choice == 5:
            player = image.load("Mängija/green.png")
            start = True
        if choice == 6:
            player = image.load("Mängija/yellow.png")
            start = True
        if choice == 7:
            player = image.load("Mängija/purple.png")
            start = True
        if choice == 8:
            player = image.load("Mängija/rose.png")
            start = True
        if choice == 9:
            choice = random.randint(1,8)
        if start:
            mängu_etapp = "genereeri"
            
    while mängu_etapp == "genereeri":
        
        #Aseta siia mängu genereerimis faas. Genereerimise ajal genereerib programm labürindi ja saadab "agendid", kes kontrollivad, et labürint on ikka läbitav.
        #Igas levelis on kive, mida koguda. Alates level 2-st tulevad sisse peidetud miinid ja alates level 5-st tulevad sisse nähtavad vaenlased.
        #Aseta start ja lõpp. Ideaalis võiks olla start all ja lõpp üleval.
        mängu_etapp = "mäng"
        
    while mängu_etapp == "mäng":
        
        #Aseta siia mäng. Kui selle ekraani suurus on 1000x1000, võiks üks ruut olla 50x50.
        #Kui mängija paneb kinni või lendab õhku, tuleb faas "game_over". Igal levelil on aega mängijal 30 minutit. Selle möödumisel on mäng läbi.
        #Punkte tuleb kogutud kivide arvust, miinide õhkulennutamisest ja vaenlaste pikali löömisest ja labürindi lahendamise kiirusest.
        punktid_kivi = random.randint(0,1000)
        punktid_miin = random.randint(0,1000)
        punktid_aeg = random.randint(0,1000)
        punktid_kokku = punktid_kivi + punktid_miin + punktid_aeg
        mängu_etapp = "game_over"
        
    while mängu_etapp == "game_over":
        hiire_x, hiire_y = mouse.get_pos()
        for i in event.get():
            if i.type == KEYUP:
                if i.key == K_RETURN:
                    if nimi == '':
                        nameerror = 1
                    else:
                        nameerror = 0
                        mängu_etapp = "salvestamine"
                if i.key == K_BACKSPACE:
                    nimi = nimi[:-1]
                elif i.key <= 127:
                    if key.get_mods() & KMOD_SHIFT:
                        nimi += chr(i.key).upper()
                    else:
                        nimi += chr(i.key)
                    if len(nimi) >= 11:
                        nimi = nimi[:-1]
            if i.type == MOUSEBUTTONUP:
                if hiire_x > 565 and hiire_x < 765 and hiire_y > 900 and hiire_y < 991:
                    if nimi == '':
                        nameerror = 1
                    else:
                        nameerror = 0
                        mängu_etapp = "salvestamine"
                if hiire_x > 276 and hiire_x < 513 and hiire_y > 900 and hiire_y < 991:
                    choice = 0
                    mängu_etapp = "menüü"
            if i.type == QUIT:
                mängu_etapp = "quit"
                meelde = "game_over"
                choice = 0
        aken.blit(läbi, [12, 0])
        aken.blit(font.render(str(punktid_kivi), 1, [255, 255, 255]), [564, 309])
        aken.blit(font.render(str(punktid_miin), 1, [255, 255, 255]), [564, 399])
        aken.blit(font.render(str(punktid_aeg), 1, [255, 255, 255]), [564, 485])
        aken.blit(font.render(str(punktid_kokku), 1, [255, 255, 255]), [564, 575])
        aken.blit(font.render(nimi, 1, [255, 255, 255]), [288, 798])
        if hiire_x > 553 and hiire_x < 753 and hiire_y > 900 and hiire_y < 991:
            aken.blit(save_yes, [565, 900])
        if hiire_x > 264 and hiire_x < 501 and hiire_y > 900 and hiire_y < 991:
            aken.blit(save_no, [276, 900])
        if nameerror == 1:
            aken.blit(font.render("You must enter your name!", 1, [255, 0, 0]), [62, 710])
        display.flip()
        
    while mängu_etapp == "salvestamine":
        scoreboard = scoreboard[:scoremax]
        scoreboard.append((punktid_kokku, nimi))
        scoreboard.sort(reverse=True)
        fail = open('highscore.pickle', 'wb')
        pickle.dump(scoreboard,fail)
        mängu_etapp = "scoreboard"
        
    while mängu_etapp == "scoreboard":
        hiire_x, hiire_y = mouse.get_pos()
        for i in event.get():
            if i.type == KEYUP:
                if i.key == K_RETURN:
                    choice = 0
                    mängu_etapp = "menüü"
            if i.type == MOUSEBUTTONUP:
                if hiire_x > 412 and hiire_x < 611 and hiire_y > 928 and hiire_y < 994:
                    choice = 0
                    mängu_etapp = "menüü"
            if i.type == QUIT:
                mängu_etapp = "quit"
                meelde = "scoreboard"
                choice = 0
        aken.blit(skoor, [12, 0])
        for t in range(len(scoreboard)):
            (punktid_kokku, nimi) = scoreboard[t]
            tabeli_y = tabeli_y + 99
            aken.blit(font.render(nimi, 1, [255, 255, 255]), [149, tabeli_y])
            aken.blit(font.render(str(punktid_kokku), 1, [255, 255, 255]), [622, tabeli_y])
        tabeli_y = 44
        if hiire_x > 412 and hiire_x < 611 and hiire_y > 928 and hiire_y < 994:
            aken.blit(scorecloser, [412, 928])
        display.flip()

    while mängu_etapp == "quit":
        hiire_x, hiire_y = mouse.get_pos()
        for i in event.get():
            if i.type == KEYUP:
                #Siin ma defineerin nooltega navigeerimist. Choice 1 on No, Choice 2 on Yes.
                if i.key == K_RIGHT:
                    if choice == 0:
                        choice = 2
                    elif choice == 1:
                        choice = 2
                    elif choice == 2:
                        choice = 1
                if i.key == K_LEFT:
                    if choice == 0:
                        choice = 1
                    elif choice == 1:
                        choice = 2
                    elif choice == 2:
                        choice = 1
                if i.key == K_RETURN:
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
            if i.type == MOUSEBUTTONUP:
                if hiire_x > 324 and hiire_x < 472 and hiire_y > 454 and hiire_y < 567:
                    #Kui vajutada No, siis mäng jätkub.
                    mängu_etapp = meelde
                if hiire_x > 552 and hiire_x < 700 and hiire_y > 454 and hiire_y < 567:
                    #Kui vajutada Yes, siis mäng sulgub.
                    if meelde == "mäng":
                        mängu_etapp = "game_over"
                    else:
                        mäng_töötab = False
                        break
                else:
                    #Muidu tühista nooleklahvidega tehtud valik.
                    choice = 0
            if i.type == QUIT:
                if meelde == "mäng":
                    mängu_etapp = "game_over"
                else:
                    mängu_etapp = 0
                    mäng_töötab = False
                    break
        #Tekita väljumist küsiv paneel ja peata mäng.
        aken.blit(küsi_väljumist, [262, 200])
        #Kui hiirega osutatakse või nooleklahviga navigeeritakse, siis see valik muutub oranžiks.
        if hiire_x > 324 and hiire_x < 472 and hiire_y > 454 and hiire_y < 567:
            aken.blit(quitno, [324, 454])
        if choice == 1:
            aken.blit(quitno, [324, 454])
        if hiire_x > 552 and hiire_x < 700 and hiire_y > 454 and hiire_y < 567:
            aken.blit(quityes, [552, 454])
        if choice == 2:
            aken.blit(quityes, [552, 454])
        display.flip()
        if mäng_töötab == False:
            #Kui mäng sulgub, siis see ikka suletakse.
            break
fail = open('highscore.pickle', 'wb')
pickle.dump(scoreboard,fail)
    
quit()
