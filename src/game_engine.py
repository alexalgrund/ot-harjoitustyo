import sys
import pygame
from database import DatabaseManager
from resources import Resources

class GameEngine:
    """Class which provides games dynamical functionalities.

    Attributes:
        resources: Picture and sound management module.
        db: Database management module.
        screen: Pygame screen display.
        clok: Game time counter.
    """

    def __init__(self):
        self.resources = Resources()
        self.db = DatabaseManager()
        self.screen = pygame.display.set_mode((940, 780))
        self.clock_time =[0, 0, 0, 0]
        self.font2 = pygame.font.SysFont("Arial", 30, bold=True)

    def draw_screen(self):
        """Displays playing field.
        """
        self.screen.fill((80, 0, 0))
        for ii in range(0, 55 * 17, 55):
            self.screen.blit(self.resources.get_image("wall"), (ii, 0))
            self.screen.blit(self.resources.get_image("wall"), (ii, 720))

    def clock(self):
        """Displays game's time counter.
        """
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
        self.end_time = f"{self.clock_time[0]:02}:{self.clock_time[1]:02}:{self.clock_time[2]:02}"

    def close_program(self):
        """Deactivates the game architecture when the player exits the game.
        """
        self.db.close_database()
        pygame.quit()
        sys.exit()
