import pygame

from code.assets import Assets
from code.level import Level
from code.menu import Menu
from code.screens import ResultScreen
from code.settings import HEIGHT, TITLE, WIDTH


class Game:
    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error:
            pass
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.assets = Assets()

    def run(self):
        state = "menu"
        while True:
            if state == "menu":
                state = Menu(self.window, self.assets).run()
            elif state == "play":
                state = Level(self.window, self.assets, number=1).run()
            elif state == "level2":
                state = Level(self.window, self.assets, number=2).run()
            elif state in ("win", "lose"):
                state = ResultScreen(self.window, self.assets).run(state)
            elif state == "quit":
                pygame.quit()
                return
            else:
                state = "menu"
