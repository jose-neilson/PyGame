import pygame

from code.assets import Assets
from code.settings import CYAN, GREEN, HEIGHT, PANEL, PANEL_BORDER, RED, WHITE, YELLOW


class ResultScreen:
    def __init__(self, window: pygame.Surface, assets: Assets):
        self.window = window
        self.assets = assets
        self.bg = assets.background("ScoreBg.png")
        self.title_font = pygame.font.SysFont("verdana", 30, bold=True)
        self.font = pygame.font.SysFont("verdana", 14)

    def run(self, result: str) -> str:
        self.assets.play_music("Score.mp3", 0.35)
        clock = pygame.time.Clock()
        won = result == "win"
        title = "VITORIA!" if won else "DERROTA"
        color = GREEN if won else RED
        subtitle = "Voce completou a demo." if won else "Tente novamente."

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "play"
                    if event.key == pygame.K_ESCAPE:
                        return "menu"

            self.window.blit(self.bg, (0, 0))
            panel = pygame.Rect(138, 74, 326, 170)
            panel_surface = pygame.Surface(panel.size, pygame.SRCALPHA)
            panel_surface.fill((*PANEL, 220))
            self.window.blit(panel_surface, panel)
            pygame.draw.rect(self.window, PANEL_BORDER, panel, 2)
            self._text(self.title_font, title, color, 170, 98)
            self._text(self.font, subtitle, WHITE, 170, 146)
            self._text(self.font, "ENTER  jogar novamente", YELLOW, 170, 186)
            self._text(self.font, "ESC    voltar ao menu", CYAN, 170, 210)
            pygame.display.flip()

    def _text(self, font: pygame.font.Font, text: str, color: tuple[int, int, int], x: int, y: int):
        surf = font.render(text, True, color)
        self.window.blit(surf, (x, y))
