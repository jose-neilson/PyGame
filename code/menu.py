import pygame

from code.assets import Assets
from code.settings import CYAN, GREEN, HEIGHT, ORANGE, TITLE, WHITE, WIDTH, YELLOW


class Menu:
    def __init__(self, window: pygame.Surface, assets: Assets):
        self.window = window
        self.assets = assets
        self.bg = assets.background("MenuBg.png")
        self.title_font = pygame.font.SysFont("lucidasanstypewriter", 42, bold=True)
        self.font = pygame.font.SysFont("lucidasanstypewriter", 16)
        self.small = pygame.font.SysFont("lucidasanstypewriter", 12)

    def run(self) -> str:
        self.assets.play_music("Menu.mp3", 0.35)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "play"
                    if event.key == pygame.K_ESCAPE:
                        return "quit"

            self.window.blit(self.bg, (0, 0))
            self._center(self.title_font, TITLE, ORANGE, HEIGHT // 2 - 72)
            self._center(self.font, "ENTER - iniciar", YELLOW, HEIGHT // 2 + 8)
            self._center(self.font, "A/D ou Setas - mover", WHITE, HEIGHT // 2 + 42)
            self._center(self.font, "Espaco - pular    J/CTRL - atirar", WHITE, HEIGHT // 2 + 64)
            self._center(self.small, "Objetivo: complete as 2 fases derrotando todos os inimigos", GREEN, HEIGHT - 34)
            self._center(self.small, "ESC - sair", CYAN, HEIGHT - 18)
            pygame.display.flip()

    def _center(self, font: pygame.font.Font, text: str, color: tuple[int, int, int], y: int):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(WIDTH // 2, y))
        self.window.blit(surf, rect)
