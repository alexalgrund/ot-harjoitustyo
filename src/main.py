import sys
import os
import sqlite3
from random import randint

import pygame

class CutleryHunt:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("The Great Cutlery Hunt of Horrible Horrors")
        self.download_pics()
        self.download_voices()
        self.create_database()
        self.screen = pygame.display.set_mode((940, 780))
        self.font1 = pygame.font.SysFont("Arial", 24)
        self.font2 = pygame.font.SysFont("Arial", 30, bold=True)
        self.font3 = pygame.font.SysFont("Arial", 40)
        self.timer = pygame.time.Clock()
        self.initial_text()

    def download_pics(self):
        images_path = os.path.join(os.path.dirname(__file__), "images")
        self.fork_pic = pygame.image.load(os.path.join(images_path, "fork.png"))
        self.knife_pic = pygame.image.load(os.path.join(images_path, "knife.png"))
        self.knight_pic = pygame.image.load(os.path.join(images_path, "knight.png"))
        self.skeleton_pic = pygame.image.load(os.path.join(images_path, "skeleton.png"))
        self.spoon_pic = pygame.image.load(os.path.join(images_path, "spoon.png"))
        self.wall_pic = pygame.image.load(os.path.join(images_path, "wall.png"))

    def download_voices(self):
        sounds_path = os.path.join(os.path.dirname(__file__), "sounds")
        self.sounds = {
            "beep": pygame.mixer.Sound(os.path.join(sounds_path, "beep.wav")),
            "crush": pygame.mixer.Sound(os.path.join(sounds_path, "crush.wav")),
            "wump": pygame.mixer.Sound(os.path.join(sounds_path, "wump.wav")),
            "surprise": pygame.mixer.Sound(os.path.join(sounds_path, "surprise.wav"))
    }

    def play_sound(self, voice_name):
        self.sounds[voice_name].play()

    def create_database(self): #Creates SQL database.
        self.db = sqlite3.connect("scoreBase.db")
        self.db.isolation_level = None

        try:
            self.db.execute("CREATE TABLE Records "
                "(id INTEGER PRIMARY KEY, score INTEGER UNIQUE, time INTEGER)")
        except sqlite3.OperationalError as e:
            if "already exists" in str(e):
                print("Table already exists.")
            else:
                print(f"Virhe: {e}")

    def draw_screen(self):
        self.screen.fill((80, 0, 0))

        for ii in range(0, 55 * 17, 55):
            self.screen.blit(self.wall_pic, (ii, 0))
            self.screen.blit(self.wall_pic, (ii, 720))

    def clock(self): #Displays the timer of main game.
        current_time = (
        f"TIME {self.clock_time[0]:02}:"
        f"{self.clock_time[1]:02}:"
        f"{self.clock_time[2]:02}"
)
        self.clock_time[3] += 1

        if self.clock_time[3] == 60:
            self.clock_time[3] = 0
            self.clock_time[2] += 1
        if self.clock_time[2] == 60:
            self.clock_time[2] = 0
            self.clock_time[1] += 1
        if self.clock_time[1] == 60:
            self.clock_time[1] = 0
            self.clock_time[0] += 1

        end_text1 = self.font2.render(current_time, True, (0, 0, 0))
        temp_surface = pygame.Surface(end_text1.get_size())
        temp_surface.fill((192, 192, 192))
        temp_surface.blit(end_text1, (0, 0))
        self.screen.blit(temp_surface, temp_surface.get_rect(center=(335, 28)))
        self.end_time = current_time[4:13]

    def show_stats(self): #Show game score statistics.
        stats = self.db.execute("SELECT ROW_NUMBER() OVER "
            "(ORDER by score DESC, time), score, time FROM Records").fetchall()
        stats_text = ["              TOP SCORES","","Rank         Points          Time"]
        for row in stats:
            row_constant = ""
            for _ in range(10-len(str(row[1]))):
                row_constant += ".."
            stats_text.append(str(f"{row[0]} ...............{row[1]}{row_constant}{row[2]}"))
        stats_text.append(" ")
        stats_text.append("        ESC =  Return Menu")

        while True:
            self.draw_screen()
            for i, text in enumerate(stats_text):
                intro_text1 = self.font2.render(text, True, (255, 0, 0))
                self.screen.blit(intro_text1, (255, 130 + i * 50))

            for keypress in pygame.event.get():
                if keypress.type == pygame.QUIT:
                    self.close_program()
                if keypress.type == pygame.KEYDOWN and keypress.key == pygame.K_ESCAPE:
                    if self.score_check:
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

        self.points = 0
        self.clock_time =[0, 0, 0, 0]
        self.score_check = False
        self.end_time = ""
        self.record_start_time = None
        self.difficulty_level = 1
        self.loop_speed = 60
        self.points_limit = 50
        self.sound_played = False

        self.x_knight = 445
        self.y_knight = 500-self.knight_pic.get_height()
        self.knight_left = 445
        self.knight_right = 495
        self.knight_down = 460
        self.knight_up = 460 - 85

        self.skeletons1 = []
        self.skeletons2 = []
        self.x_fork = randint(40, 860)
        self.y_fork = randint(80, 660)

        self.x_knife = randint(1000, 1000)
        self.y_knife = randint(80, 660)
        self.knife_line = randint(15, 25)
        self.knife_repeat = True

        self.x_spoon = randint(1000, 1000)
        self.y_spoon = randint(80, 660)
        self.spoon_line = randint(40, 55)
        self.spoon_repeat = True
        self.arrow_right = False
        self.arrow_left = False
        self.arrow_up = False
        self.arrow_down = False

    def initial_text(self): #Displays the introduction texts of game.
        while True:
            self.draw_screen()
            intro_text1 = self.font3.render(
                "The Great Cutlery Hunt of Horrible Horrors", True, (255, 0, 0))
            self.screen.blit(intro_text1, intro_text1.get_rect(center=(470, 220)))
            intro_text2 = ["In this game you face horrible horrors "
            "while hunting precious silver cutleries.",
            "Use arrowkeys to gahter cutleries with knight "
            "while avoiding horrible horrors. ",
            "Game ends when horrible horror reaches you."]

            table_count = self.db.execute("SELECT COUNT(score) FROM Records").fetchone()[0]
            if table_count > 0:
                intro_text3 = "Enter = New game   L-Shift = Show Top Scores   ESC = Exit"
            else:
                intro_text3 = "Enter = New game"

            i = 0
            ii = 320
            while i < len(intro_text2):
                intro_plat1 = self.font1.render(intro_text2[i], True, (255, 0, 0))
                self.screen.blit(intro_plat1, intro_plat1.get_rect(center=(470, ii)))
                intro_plat2 = self.font2.render(intro_text3, True, (255, 0, 0))
                self.screen.blit(intro_plat2, intro_plat2.get_rect(center=(470, 510)))
                i += 1
                ii += 50

            i = 0
            ii = 420
            while i < 3:
                self.screen.blit(self.fork_pic, self.fork_pic.get_rect(center=(ii, 610)))
                self.screen.blit(self.skeleton_pic, self.skeleton_pic.get_rect(center=(370, 610)))
                self.screen.blit(self.skeleton_pic, self.skeleton_pic.get_rect(center=(570, 610,)))
                i += 1
                ii += 50

            for keypress in pygame.event.get():
                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_RETURN:
                        self.cycle()
                    if table_count > 0:
                        if keypress.key == pygame.K_LSHIFT:
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

            end_text1 = self.font2.render("POINTS " + str(self.points), True, (0, 0, 0))
            temp_surface = pygame.Surface(end_text1.get_size())
            temp_surface.fill((192, 192, 192))
            temp_surface.blit(end_text1, (0, 0))
            self.screen.blit(temp_surface, temp_surface.get_rect(center=(117, 28)))

            end_text1 = self.font3.render("Game starts in " + str(self.count), True, (255, 0, 0))
            self.screen.blit(end_text1, end_text1.get_rect(center=(470, 370)))
            self.screen.blit(self.knight_pic, (self.x_knight, self.y_knight))

            self.count-=1

            pygame.display.flip()
            self.timer.tick(1)

    def maingame(self): #Starts the game.
        while True:
            self.draw_screen()
            self.clock()

            point_text = self.font2.render("POINTS " + str(self.points), True, (0, 0, 0))
            temp_surface1 = pygame.Surface(point_text.get_size())
            temp_surface1.fill((192, 192, 192))
            temp_surface1.blit(point_text, (0, 0))
            self.screen.blit(temp_surface1, temp_surface1.get_rect(center=(117, 28)))

            if self.points == self.points_limit:
                self.difficulty_level += 1
                self.loop_speed += 10
                self.points_limit += 50
                if self.record_start_time is None:
                    self.record_start_time = pygame.time.get_ticks()
            if self.record_start_time and pygame.time.get_ticks() - self.record_start_time <= 3000:
                self.play_sound("surprise")
                new_level_text = self.font2.render(f"LEVEL {self.difficulty_level}",
                True, (0, 0, 0))
                new_level_rect = new_level_text.get_rect(center=(self.screen.get_width()
                 // 2, self.screen.get_height() // 2))
                self.screen.blit(new_level_text, new_level_rect)
            if self.record_start_time and pygame.time.get_ticks() - self.record_start_time > 3000:
                self.record_start_time = None

            self.screen.blit(self.knight_pic, (self.x_knight, self.y_knight))
            self.screen.blit(self.fork_pic, (self.x_fork, self.y_fork))
            self.screen.blit(self.knife_pic, (self.x_knife, self.y_knife))
            self.screen.blit(self.spoon_pic, (self.x_spoon, self.y_spoon))

            for keypress in pygame.event.get():
                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_LEFT:
                        self.arrow_left = True
                    if keypress.key == pygame.K_RIGHT:
                        self.arrow_right = True

                if keypress.type == pygame.KEYUP:
                    if keypress.key == pygame.K_LEFT:
                        self.arrow_left = False
                    if keypress.key == pygame.K_RIGHT:
                        self.arrow_right = False

                if keypress.type == pygame.KEYDOWN:
                    if keypress.key == pygame.K_UP:
                        self.arrow_up = True
                    if keypress.key == pygame.K_DOWN:
                        self.arrow_down = True

                if keypress.type == pygame.KEYUP:
                    if keypress.key == pygame.K_UP:
                        self.arrow_up = False
                    if keypress.key == pygame.K_DOWN:
                        self.arrow_down = False

                if keypress.type == pygame.QUIT:
                    self.close_program()

            if self.arrow_right and self.x_knight < 890:
                self.x_knight += 5
                self.knight_left += 5
                self.knight_right += 5

            if self.arrow_left and self.x_knight > 0:
                self.x_knight -= 5
                self.knight_left -= 5
                self.knight_right -= 5

            if self.arrow_up and self.y_knight > 60:
                self.y_knight -= 5
                self.knight_down -= 5
                self.knight_up -= 5

            if self.arrow_down and self.y_knight < 640:
                self.y_knight += 5
                self.knight_down += 5
                self.knight_up += 5

            if self.x_fork >= self.knight_left and self.x_fork <= self.knight_right \
            and self.knight_down >= self.y_fork and self.knight_up <= self.y_fork:
                self.x_fork = randint(40, 860)
                self.y_fork = randint(80, 660)
                self.points += 1
                self.play_sound("wump")

            if self.x_knife >= self.knight_left and self.x_knife <= self.knight_right \
            and self.knight_down >= self.y_knife and self.knight_up <= self.y_knife:
                self.x_knife = randint(1000, 1000)
                self.y_knife = randint(1000, 1000)
                self.knife_line = self.knife_line + randint(10, 25)
                self.points += 1
                self.play_sound("wump")
                self.knife_repeat = True

            if self.points == self.knife_line and self.knife_repeat is True:
                self.x_knife = randint(40, 860)
                self.y_knife = randint(80, 660)
                self.knife_repeat = False

            if self.x_spoon >= self.knight_left and self.x_spoon <= self.knight_right \
            and self.knight_down >= self.y_spoon and self.knight_up <= self.y_spoon:
                self.x_spoon = randint(1000, 1000)
                self.y_spoon = randint(1000, 1000)
                self.spoon_line = self.spoon_line + randint(40, 55)
                self.points += 1
                self.play_sound("wump")

            if self.points == self.spoon_line and self.spoon_repeat is True:
                self.x_spoon = randint(40, 860)
                self.y_spoon = randint(80, 660)
                self.spoon_repeat = False

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
                if self.knight_up <= y <= self.knight_down and \
                    self.knight_left <= x <= self.knight_right:
                    self.play_sound("crush")
                    pygame.time.wait(1200)
                    self.end_text()
                if x >= 1000:
                    x = randint(-1500, -100)
                    y = randint(60, 650)
                self.skeletons1[i] = (x, y)
                self.screen.blit(self.skeleton_pic, (x, y))

            for i in range(5):
                x1, y1 = self.skeletons2[i]
                x1 -= 5
                if self.knight_up <= y1 <= self.knight_down \
                    and self.knight_left <= x1 <= self.knight_right:
                    self.play_sound("crush")
                    pygame.time.wait(1200)
                    self.end_text()
                if x1 <= -100:
                    x1 = randint(1000, 2400)
                    y1 = randint(60, 650)
                self.skeletons2[i] = (x1, y1)
                self.screen.blit(self.skeleton_pic, (x1, y1))

            pygame.display.flip()
            self.timer.tick(self.loop_speed)

    def end_text(self): #Displays the player's score, game time
        # and gives player a possibility to start the game again or close program.
        self.score_check = True
        table_count = self.db.execute("SELECT COUNT(score) FROM Records").fetchone()[0]
        try:
            if table_count > 0:
                last_score = self.db.execute(
                    "SELECT score FROM Records ORDER BY score LIMIT 1").fetchone()[0]
                last_time = self.db.execute(
                    "SELECT time FROM Records ORDER BY score LIMIT 1").fetchone()[0]
            if table_count < 5:
                self.db.execute(
                        "INSERT INTO Records (score, time) VALUES (?, ?)",
                        [self.points, self.end_time])
            elif table_count == 5 and last_score < self.points:
                self.db.execute(
                    "DELETE FROM Records WHERE score=? AND time=?",
                    [last_score, last_time ])
                self.db.execute(
                    "INSERT INTO Records (score, time) VALUES (?, ?)",
                    [self.points, self.end_time])

        except sqlite3.OperationalError as e:
            if "Table error" in str(e):
                print("Table error.")
            else:
                print(f"Virhe: {e}")

        while True:
            self.draw_screen()

            if self.points == 1:
                points_anc = " point in"
            else:
                points_anc = " points in"

            if self.points == self.db.execute("SELECT MAX(score) FROM Records").fetchone()[0]:
                new_record_text = self.font3.render("NEW RECORD", True, (255, 0, 0))
                self.screen.blit(new_record_text, new_record_text.get_rect(center=(470, 120)))
                if self.sound_played is False:
                    self.play_sound("surprise")
                    self.sound_played = True

            end_text1 = self.font3.render("GAME OVER", True, (255, 0, 0))
            end_text2 = self.font3.render("You got " +
            str(self.points) + points_anc + str(self.end_time), True, (255, 0, 0))
            end_text3 = self.font2.render
            ("Enter = New game   L-Shift = Show Top Scores   ESC = Exit", True, (255, 0, 0))

            self.screen.blit(end_text1, end_text1.get_rect(center=(470, 290)))
            self.screen.blit(end_text2, end_text2.get_rect(center=(470, 370)))
            self.screen.blit(end_text3, end_text3.get_rect(center=(470, 560)))


            i = 0
            ii = 420
            while i < 3:
                self.screen.blit(self.skeleton_pic, self.skeleton_pic.get_rect(center=(ii, 200)))
                self.screen.blit(self.skeleton_pic, self.skeleton_pic.get_rect(center=(ii, 450)))
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
