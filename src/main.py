import pygame
import sys
import sqlite3
from random import randint

class CutleryHunt:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("The Great Cutlery Hunt of Horrible Horrors")
        
        self.download_pics()
        self.download_voices()
        self.create_database()
        self.initialize_game()
        self.initial_text()

    def download_pics(self): #Downloads pictures used in game
        self.forkPic = pygame.image.load("fork.png")
        self.knifePic = pygame.image.load("knife.png")
        self.knightPic = pygame.image.load("knight.png")
        self.skeletonPic = pygame.image.load("skeleton.png")
        self.spoonPic = pygame.image.load("spoon.png")
        self.wallPic = pygame.image.load("wall.png")
    
    def download_voices(self):
        self.sounds = {
            "beep": pygame.mixer.Sound("beep.wav"),
            "crush": pygame.mixer.Sound("crush.wav"),
            "wump": pygame.mixer.Sound("wump.wav"),
        }

    def play_sound(self, voice_name):
        self.sounds[voice_name].play()
    
    def create_database(self): #Creates SQL database.
        self.db = sqlite3.connect("scoreBase.db")
        self.db.isolation_level = None

        try:
            self.db.execute("CREATE TABLE Records (id INTEGER PRIMARY KEY, score INTEGER UNIQUE, time INTEGER)")
        except:
            pass

    def draw_screen(self):
        self.screen.fill((80, 0, 0))

        for ii in range(0, 55 * 17, 55):
            self.screen.blit(self.wallPic, (ii, 0))
            self.screen.blit(self.wallPic, (ii, 720))

    
    def clock(self): #Displays the timer of main game.
        currentTime = f"TIME {self.clockTime[0]:02}:{self.clockTime[1]:02}:{self.clockTime[2]:02}"
        self.clockTime[3] += 1

        if self.clockTime[3] == 60:
            self.clockTime[3] = 0
            self.clockTime[2] += 1
        if self.clockTime[2] == 60:
            self.clockTime[2] = 0
            self.clockTime[1] += 1
        if self.clockTime[1] == 60:
            self.clockTime[1] = 0
            self.clockTime[0] += 1
        
        endText1 = self.font2.render(currentTime, True, (0, 0, 0))
        temp_surface = pygame.Surface(endText1.get_size())
        temp_surface.fill((192, 192, 192))
        temp_surface.blit(endText1, (0, 0))
        self.screen.blit(temp_surface, temp_surface.get_rect(center=(335, 28)))

        self.endTime = currentTime[4:13]
    
    def show_stats(self): #Show game score statistics.
        stats = self.db.execute("SELECT ROW_NUMBER() OVER (ORDER by score DESC, time), score, time FROM Records").fetchall()
        statsText = ["              TOP SCORES","","Rank         Points          Time"]
        for row in stats:
            rowConstant = ""
            for _ in range(10-len(str(row[1]))):
                rowConstant += ".."
            statsText.append(str(f"{row[0]} ...............{row[1]}{rowConstant}{row[2]}"))
        statsText.append(" ")
        statsText.append("        ESC =  Return Menu")
 
        while True:
            self.draw_screen()

            for i, text in enumerate(statsText):
                introText1 = self.font2.render(text, True, (255, 0, 0))
                self.screen.blit(introText1, (255, 130 + i * 50))

            for keypress in pygame.event.get():
                if keypress.type == pygame.QUIT:
                    self.close_program()
                    return
                if keypress.type == pygame.KEYDOWN and keypress.key == pygame.K_ESCAPE:
                    if self.scoreCheck:
                        self.end_text()
                    else:
                        self.initial_text()

            pygame.display.flip()
            self.timer.tick(60)

    def cycle(self): #A loop used to start a new game.
        self.initialize_game()
        self.countdown()
        self.maingame()
    
    def initialize_game(self): #Initialize all essential variables of game.
        self.screen = pygame.display.set_mode((940, 780))
        self.font1 = pygame.font.SysFont("Arial", 24)
        self.font2 = pygame.font.SysFont("Arial", 30, bold=True)       
        self.font3 = pygame.font.SysFont("Arial", 40)
        self.points = 0
        self.clockTime =[0, 0, 0, 0]
        self.scoreCheck = False
        self.endTime = ""

        self.xKnight = 445
        self.yKnight = 500-self.knightPic.get_height()
        self.knightLeft = 445
        self.knightRight = 495
        self.knightDown = 460
        self.knightUp = 460 - 85

        self.skeletons1 = []
        self.skeletons2 = []
        
        self.xFork = randint(40, 860)
        self.yFork = randint(80, 660)

        self.xKnife = randint(1000, 1000)
        self.yKnife = randint(80, 660)
        self.knifeLine = randint(15, 25)
        self.knifeRepeat = True

        self.xSpoon = randint(1000, 1000)
        self.ySpoon = randint(80, 660)
        self.spoonLine = randint(40, 55)
        self.spoonRepeat = True
            
        self.arrowRight = False
        self.arrowLeft = False
        self.arrowUp = False
        self.arrowDown = False
            
        self.timer = pygame.time.Clock()

    def initial_text(self): #Displays the introduction texts of game.
        while True:
            self.draw_screen()
            introText1 = self.font3.render("The Great Cutlery Hunt of Horrible Horrors", True, (255, 0, 0))
            self.screen.blit(introText1, introText1.get_rect(center=(470, 220))) 
            introText2 = ["In this game you face horrible horrors while hunting precious silver cutleries.",
            "Use arrowkeys to gahter cutleries with knight while avoiding horrible horrors.",
            "Game ends when horrible horror reaches you."]

            tableCount = self.db.execute("SELECT COUNT(score) FROM Records").fetchone()[0]
            if tableCount > 0:
                introText3 = "F2 = New game   F3 = Show Top Scores"
            else:
                introText3 = "F2 = New game"

            i = 0
            ii = 320
            while i < len(introText2):
                introPlat1 = self.font1.render(introText2[i], True, (255, 0, 0))
                self.screen.blit(introPlat1, introPlat1.get_rect(center=(470, ii)))
                introPlat2 = self.font2.render(introText3, True, (255, 0, 0))
                self.screen.blit(introPlat2, introPlat2.get_rect(center=(470, 510)))
                i += 1
                ii += 50
                
            i = 0
            ii = 420
            while i < 3:
                self.screen.blit(self.forkPic, self.forkPic.get_rect(center=(ii, 610)))
                self.screen.blit(self.skeletonPic, self.skeletonPic.get_rect(center=(370, 610)))
                self.screen.blit(self.skeletonPic, self.skeletonPic.get_rect(center=(570, 610,)))
                i += 1
                ii += 50

            for keypress in pygame.event.get():
                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_F2:
                        self.cycle()
                    if tableCount > 0:
                        if keypress.key == pygame.K_F3:
                            self.show_stats()
                    if keypress.key == pygame.K_ESCAPE:
                        self.close_program()
                if keypress.type == pygame.QUIT:
                    self.close_program()
            
            pygame.display.flip()
            self.timer.tick(60)

    def countdown(self): #Gives 5 seconds time for player to get ready.
        self.count = 5
        while self.count > -1:
            self.draw_screen()
            self.clock()
            if self.count <= 4:
                self.play_sound("beep")

            endText1 = self.font2.render("POINTS " + str(self.points), True, (0, 0, 0))
            temp_surface = pygame.Surface(endText1.get_size())
            temp_surface.fill((192, 192, 192))
            temp_surface.blit(endText1, (0, 0))
            self.screen.blit(temp_surface, temp_surface.get_rect(center=(117, 28)))

            endText1 = self.font3.render("Game starts in " + str(self.count), True, (255, 0, 0))
            self.screen.blit(endText1, endText1.get_rect(center=(470, 370)))
            self.screen.blit(self.knightPic, (self.xKnight, self.yKnight))

            self.count -= 1
 
            pygame.display.flip()
            self.timer.tick(1)
            
    def maingame(self): #Starts the game.
        while True:
            self.draw_screen()
            self.clock()

            pointText = self.font2.render("POINTS " + str(self.points), True, (0, 0, 0))
            temp_surface1 = pygame.Surface(pointText.get_size())
            temp_surface1.fill((192, 192, 192))
            temp_surface1.blit(pointText, (0, 0))
            self.screen.blit(temp_surface1, temp_surface1.get_rect(center=(117, 28)))

            self.screen.blit(self.knightPic, (self.xKnight, self.yKnight))
            self.screen.blit(self.forkPic, (self.xFork, self.yFork))
            self.screen.blit(self.knifePic, (self.xKnife, self.yKnife))
            self.screen.blit(self.spoonPic, (self.xSpoon, self.ySpoon))


            for keypress in pygame.event.get():
                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_LEFT:
                        self.arrowLeft = True
                    if keypress.key == pygame.K_RIGHT:
                        self.arrowRight = True

                if keypress.type == pygame.KEYUP:
                    if keypress.key == pygame.K_LEFT:
                        self.arrowLeft = False
                    if keypress.key == pygame.K_RIGHT:
                        self.arrowRight = False
                
                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_UP:
                        self.arrowUp = True
                    if keypress.key == pygame.K_DOWN:
                        self.arrowDown = True
                
                if keypress.type == pygame.KEYUP:
                    if keypress.key == pygame.K_UP:
                        self.arrowUp = False
                    if keypress.key == pygame.K_DOWN:
                        self.arrowDown = False
            
                if keypress.type == pygame.QUIT:
                    self.close_program()

        
            if self.arrowRight and self.xKnight < 890:
                self.xKnight += 5
                self.knightLeft += 5
                self.knightRight += 5

            if self.arrowLeft and self.xKnight > 0:
                self.xKnight -= 5
                self.knightLeft -= 5
                self.knightRight -= 5

            if self.arrowUp and self.yKnight > 60:
                self.yKnight -= 5
                self.knightDown -= 5
                self.knightUp -= 5

            if self.arrowDown and self.yKnight < 640:
                self.yKnight += 5
                self.knightDown += 5
                self.knightUp += 5


            if self.xFork >= self.knightLeft and self.xFork <= self.knightRight and self.knightDown >= self.yFork and self.knightUp <= self.yFork:
                self.xFork = randint(40, 860)
                self.yFork = randint(80, 660)
                self.points += 1
                self.play_sound("wump")

            if self.xKnife >= self.knightLeft and self.xKnife <= self.knightRight and self.knightDown >= self.yKnife and self.knightUp <= self.yKnife:
                self.xKnife = randint(1000, 1000)
                self.yKnife = randint(1000, 1000)
                self.knifeLine = self.knifeLine + randint(10, 25)
                self.points += 1
                self.play_sound("wump")
                self.knifeRepeat = True

            if self.points == self.knifeLine and self.knifeRepeat == True:
                self.xKnife = randint(40, 860)
                self.yKnife = randint(80, 660)
                self.knifeRepeat = False

            if self.xSpoon >= self.knightLeft and self.xSpoon <= self.knightRight and self.knightDown >= self.ySpoon and self.knightUp <= self.ySpoon:
                self.xSpoon = randint(1000, 1000)
                self.ySpoon = randint(1000, 1000)
                self.spoonLine = self.spoonLine + randint(40, 55)
                self.points += 1
                self.play_sound("wump")

            if self.points == self.spoonLine and self.spoonRepeat == True:
                self.xSpoon = randint(40, 860)
                self.ySpoon = randint(80, 660)
                self.spoonRepeat = False


            for _ in range(5):
                x = randint(-1500, -100)
                y = randint(60, 650)
                self.skeletons1.append((x, y))
            
            for _ in range(5):
                x1 = randint(1000, 2400)
                y1 = randint(60, 650)
                self.skeletons2.append((x1, y1)) 
            
            for i in range(5):
                x, y = self.skeletons1[i]
                if x < 1000:
                    x += 5
                if y <= self.knightDown and y >= self.knightUp and x >= self.knightLeft and x <= self.knightRight:
                    self.play_sound("crush")
                    pygame.time.wait(1200)
                    self.end_text()
                if x >= 1000:
                    x = randint(-1500, -100)
                    y = randint(60, 650)
                self.skeletons1[i] = (x, y)
                self.screen.blit(self.skeletonPic, (x, y))
            
            for i in range(5):
                x1, y1 = self.skeletons2[i]
                x1 -= 5
                if y1 <= self.knightDown and y1 >= self.knightUp and x1 >= self.knightLeft and x1 <= self.knightRight:
                    self.play_sound("crush")
                    pygame.time.wait(1200)
                    self.end_text()
                if x1 <= -100:
                    x1 = randint(1000, 2400)
                    y1 = randint(60, 650)
                self.skeletons2[i] = (x1, y1)
                self.screen.blit(self.skeletonPic, (x1, y1))
            
            pygame.display.flip()
            self.timer.tick(60)
    
    def end_text(self): #Displays the player's score, game time and gives player a possibility to start the game again or close program.
        self.scoreCheck = True
        tableCount = self.db.execute("SELECT COUNT(score) FROM Records").fetchone()[0]
        try:
            if tableCount > 0:
                lastScore = self.db.execute("SELECT score FROM Records ORDER BY score LIMIT 1").fetchone()[0]
                lastTime = self.db.execute("SELECT time FROM Records ORDER BY score LIMIT 1").fetchone()[0]
            if tableCount < 5:
                    self.db.execute("INSERT INTO Records (score, time) VALUES (?, ?)", [self.points, self.endTime])
            elif tableCount == 5 and lastScore < self.points:
                self.db.execute("DELETE FROM Records WHERE score=? AND time=?", [lastScore, lastTime ])
                self.db.execute("INSERT INTO Records (score, time) VALUES (?, ?)", [self.points, self.endTime])
        except:
            pass

        while True:
            self.draw_screen()

            if self.points == 1:
                pointsAnc = " point in"
            else:
                pointsAnc = " points in"

            endText1 = self.font3.render("GAME OVER ", True, (255, 0, 0))
            endText2 = self.font3.render("You got " + str(self.points) + pointsAnc + str(self.endTime), True, (255, 0, 0))   
            endText3 = self.font2.render("F2 = New game   F3 = Show Top Scores   ESC = Exit", True, (255, 0, 0))
            self.screen.blit(endText1, endText1.get_rect(center=(470, 290)))
            self.screen.blit(endText2, endText2.get_rect(center=(470, 370)))
            self.screen.blit(endText3, endText3.get_rect(center=(470, 560)))

            i = 0
            ii = 420
            while i < 3:
                self.screen.blit(self.skeletonPic, self.skeletonPic.get_rect(center=(ii, 200)))
                self.screen.blit(self.skeletonPic, self.skeletonPic.get_rect(center=(ii, 450)))
                i += 1
                ii += 50
            
            for keypress in pygame.event.get():
                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_RETURN:
                        self.cycle()
                    if keypress.key == pygame.K_LSHIFT:
                        self.show_stats()
                    if keypress.key == pygame.K_ESCAPE:
                        self.close_program()
                if keypress.type == pygame.QUIT:
                    self.close_program()
            
            pygame.display.flip()
            self.timer.tick(60)
    
    def close_program(self):
        self.db.close()
        pygame.quit()
        sys.exit()
    
if __name__ == "__main__":
    CutleryHunt()