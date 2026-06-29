import pygame

from code.assets import Assets
from code.settings import AUTHOR, CYAN, GREEN, HEIGHT, PANEL, PANEL_BORDER, RU, TITLE, WHITE, WIDTH, YELLOW


class Menu:
    def __init__(self, window: pygame.Surface, assets: Assets):
        self.window = window
        self.assets = assets
        self.bg = assets.background("MenuBg.png")
        self.title_font = pygame.font.SysFont("verdana", 26, bold=True)
        self.font = pygame.font.SysFont("verdana", 13)
        self.small = pygame.font.SysFont("verdana", 10)

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

            self._draw()
            pygame.display.flip()

    def _draw(self):
        self.window.blit(self.bg, (0, 0))
        panel = pygame.Rect(18, 22, 318, HEIGHT - 44)
        panel_surface = pygame.Surface(panel.size, pygame.SRCALPHA)
        panel_surface.fill((*PANEL, 216))
        self.window.blit(panel_surface, panel)
        pygame.draw.rect(self.window, PANEL_BORDER, panel, 2)

        self._text(self.title_font, TITLE, WHITE, 38, 42)
        self._text(self.small, "Aventura plataforma 2D", CYAN, 40, 80)
        pygame.draw.line(self.window, PANEL_BORDER, (40, 106), (304, 106), 2)

        self._text(self.font, "ENTER", YELLOW, 44, 128)
        self._text(self.font, "Iniciar", WHITE, 134, 128)
        self._text(self.font, "A/D", YELLOW, 44, 156)
        self._text(self.font, "Mover", WHITE, 134, 156)
        self._text(self.font, "ESPACO", YELLOW, 44, 184)
        self._text(self.font, "Pular", WHITE, 134, 184)
        self._text(self.font, "J/CTRL", YELLOW, 44, 212)
        self._text(self.font, "Atirar", WHITE, 134, 212)

        self._text(self.small, "Complete 2 fases.", GREEN, 40, HEIGHT - 84)
        self._text(self.small, "Derrote todos os inimigos.", GREEN, 40, HEIGHT - 68)
        self._text(self.small, "Alcance a bandeira.", GREEN, 40, HEIGHT - 52)
        self._text(self.small, AUTHOR, WHITE, 40, HEIGHT - 34)
        self._text(self.small, RU, CYAN, 238, HEIGHT - 34)

    def _text(self, font: pygame.font.Font, text: str, color: tuple[int, int, int], x: int, y: int):
        surf = font.render(text, True, color)
        self.window.blit(surf, (x, y))
