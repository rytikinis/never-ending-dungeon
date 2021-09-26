import pygame
import sys
import random
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

#Veriables

font = pygame.font.SysFont('Pixel', 30)
in_ = 'menu'

#Window

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Never ending dungeon') 

#Menu

class menu():
    class startmenu():
        def __init__(self):
            self.at = 1
            self.title = pygame.image.load('Title.png').convert()
        def loop(self):
            global in_, livesdw, tiles, player
            win.blit(pygame.transform.scale(self.title, (500, 200)), (100, 50))
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.at == 0:
                self.at += 1
            if key[pygame.K_DOWN] and self.at == 1:
                self.at -= 1
            if self.at == 0:
                win.blit((font.render('PLAY', False, (0, 0, 0))), (360, 300))
                win.blit((font.render('QUIT', False, (255, 255, 255))), (360, 320))
            if self.at == 1:
                win.blit((font.render('PLAY', False, (255, 255, 255))), (360, 300))
                win.blit((font.render('QUIT', False, (0, 0, 0))), (360, 320))
            if self.at == 1 and key[pygame.K_SPACE]:
                in_ = 'game'
                tiles = game.tiles()
                player = game.player()
                lives = game.lives()
                lives.livesl = 3
                lives.livesl = 3
                player.score = 0
                pygame.mixer.music.load('Select.wav')
                pygame.mixer.music.play()
            if self.at == 0 and key[pygame.K_SPACE]:
                pygame.mixer.music.load('Select.wav')
                pygame.mixer.music.play()
                pygame.quit()
                sys.exit()
    class restartmenu(): 
        def __init__(self):
            self.at = 1
        def loop(self):
            global in_, livesdw, tiles, player
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.at == 0:
                self.at += 1
            if key[pygame.K_DOWN] and self.at == 1:
                self.at -= 1
            if self.at == 0:
                win.blit((font.render('Score :'+ str(player.score), False, (0, 0, 0))), (350, 280))
                win.blit((font.render('RESTART', False, (0, 0, 0))), (380, 300))
                win.blit((font.render('MAIN MENU', False, (255, 255, 255))), (360, 320))
            if self.at == 1:
                win.blit((font.render('Score :'+ str(player.score), False, (0, 0, 0))), (350, 280))
                win.blit((font.render('RESTART', False, (255, 255, 255))), (380, 300))
                win.blit((font.render('MAIN MENU', False, (0, 0, 0))), (360, 320))
            if self.at == 1 and key[pygame.K_SPACE]:
                in_ = 'game'
                tiles = game.tiles()
                player = game.player()
                lives = game.lives()
                lives.livesl = 3
                player.score = 0
                pygame.mixer.music.load('Select.wav')
                pygame.mixer.music.play()
            if self.at == 0 and key[pygame.K_SPACE]:
                pygame.mixer.music.load('Select.wav')
                pygame.mixer.music.play()
                in_ = 'menu'
                time.sleep(0.2)
#Game

class game():
    class tiles():
        def __init__(self):
            self.cx = 0
            self.cy = 0
            self.brick = pygame.image.load('Brick.png').convert()
            self.doorsf = pygame.image.load('Doors.png').convert()
            self.coin = pygame.image.load('Coin.png').convert()
            self.tiles = list()
            self.x = list()
            self.y = list()
            self.type = list()
            self.coins = list()
            self.regenmap()
        def regenmap(self):
            if self.x:
                self.x.clear()
                self.y.clear()
                self.type.clear()
            self.x = list()
            self.y = list()
            self.type = list()
            lives.livesl = 3
            for a in range(15000, 0, -50):
                if a != 350 and a != 15000:
                    if not a - self.x[len(self.x) - 1] == -100: #and a - self.x[len(self.x) - 1] == 500:
                        if random.randint(0, 1) == 1:
                            for b in range(550, 400, -50):
                                self.x.append(a)
                                self.y.append(b)
                                self.type.append('brick')
                                if random.randint(0, 1) == 1:
                                    self.x.append(a)
                                    self.y.append(400)
                                    self.type.append('coin')
                elif a == 350:
                    for b in range(550, 400, - 50):
                        self.x.append(a)
                        self.y.append(b)
                        self.type.append('brick')
                elif a == 15000:
                    for a in range(550, 400, -50):
                        self.x.append(15000)
                        self.y.append(a)
                        if a != 450:
                            self.type.append('brick')
                        else:
                            self.type.append('doors')
            for a in range(16000, -1000, -50):
                self.x.append(a)
                self.y.append(0)
                self.type.append('brick')
                if random.randint(0, 1) == 1:
                    self.x.append(a)
                    self.y.append(50)
                    self.type.append('brick')
        def loop(self):
            self.tiles.clear()
            self.coins.clear()
            for a in range(len(self.x)):
                if not player.x - self.x[a] > 400 and not player.x - self.x[a] < -500:
                    if self.type[a] == 'brick':
                        self.tiles.append(win.blit((self.brick), (self.x[a] - self.cx, self.y[a] - self.cy)))
                    if self.type[a] == 'doors':
                        self.doors = win.blit((self.doorsf), (self.x[a] - self.cx, self.y[a] - self.cy - 100))
                        self.tiles.append(win.blit((self.brick), (self.x[a] - self.cx, self.y[a] - self.cy)))
                    # if self.type[a] == 'coin':
                    #     self.coins.append(win.blit((self.coin), (self.x[a] - self.cx, self.y[a] - self.cy)))
            for a in range(self.x[len(self.tiles) - 1] + 50, self.x[len(self.tiles) - 1] + 50, -50):
                if random.randint(0, 1) == 1:
                    for b in range(550, 400, - 50):
                        self.x.append(a)
                        self.y.append(b)
    class player(): 
        def __init__(self):
            self.highscore = 0
            self.score = 0
            self.roomspassed = 0
            self.collected = list()
            self.x = 350
            self.y = 300
            self.yvel = 0
            self.player = pygame.image.load('Ninja.png').convert_alpha()
            self.right = False
        def move(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d] and not self.c2.collidelistall(tiles.tiles) and self.y < 580:
                self.x += 2
                tiles.cx += 2
                self.right = False
            elif key[pygame.K_a] and not self.c2.collidelistall(tiles.tiles) and self.y < 580:
                self.x -= 2
                tiles.cx -= 2
                self.right = True
            if key[pygame.K_a] and self.c2.collidelistall(tiles.tiles):
                self.x += 2
                tiles.cx += 2
            if key[pygame.K_d] and self.c2.collidelistall(tiles.tiles):
                self.x -= 2
                tiles.cx -= 2
        def gravyti(self):
            key = pygame.key.get_pressed()
            if not self.c.collidelistall(tiles.tiles):
                if self.yvel < 3:
                    self.yvel += 0.05
            elif self.c.collidelistall(tiles.tiles) and not key[pygame.K_w]:
                self.yvel = 0
            self.y += self.yvel
        def jump(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and self.ninja.collidelistall(tiles.tiles) and not self.c2.collidelistall(tiles.tiles) and self.y < 590:
                pygame.mixer.music.load('Jump.wav')
                pygame.mixer.music.play()
                self.yvel = -3
            if self.c3.collidelistall(tiles.tiles):
                self.yvel = 0
            if key[pygame.K_w] and self.ninja.collidelistall(tiles.tiles) and self.c2.collidelistall(tiles.tiles) and self.y < 590:
                self.yvel = 3
        def next_room(self):
            self.x = 350
            self.y = 300
            self.yvel = 0
            tiles.cx = 0
            tiles.cy = 0
            lives.livesl = 3
            self.roomspassed += 1
            tiles.regenmap()
        def loop(self):
            global in_
            key = pygame.key.get_pressed()
            self.c = pygame.Rect(self.x + 10 - tiles.cx, self.y + 45, 30, 5)
            self.c2 = pygame.Rect(self.x - tiles.cx, self.y + 20, 50, 20)
            self.c3 = pygame.Rect(self.x + 10 - tiles.cx, self.y, 30, 5)
            self.ninja = win.blit(pygame.transform.flip(self.player, self.right, False), (self.x - tiles.cx, self.y - tiles.cy))
            self.move()
            self.jump()
            self.gravyti()
            if key[pygame.K_SPACE] and self.x > 14950 and self.x < 15050:
                self.next_room()
            if self.y >= 600 and lives.livesl:
                lives.livesl -= 1
                self.yvel = -6
                pygame.mixer.music.load('Ded.wav')
                pygame.mixer.music.play()
                self.y = 601
                time.sleep(0.2)
            elif not lives.livesl and self.y >= 600:
                self.score = self.x + self.roomspassed * 10000
                pygame.mixer.music.load('Ded.wav')
                pygame.mixer.music.play()
                in_ = 'restart menu'
    class lives():
        def __init__(self):
            self.lives = pygame.transform.scale(pygame.image.load('Ninja.png'), (30, 30)).convert_alpha()
            self.livesl = 3
        def loop(self):
            self.x = 50
            for a in range(self.livesl):
                win.blit((self.lives), (self.x, 50))
                self.x += 50

#Sprites

lives = game.lives()
tiles = game.tiles()
player = game.player()
startmenu = menu.startmenu()
restartmenu = menu.restartmenu()
# coins = game.coins()


#Loop

while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if in_ == 'game':
        win.fill((0, 0, 0))
        tiles.loop()
        player.loop()
        lives.loop()
    elif in_ == 'menu':
        win.fill((32, 40, 78))
        startmenu.loop()
    elif in_ == 'restart menu':
        win.fill((32, 40, 78))
        restartmenu.loop()
    pygame.display.update()