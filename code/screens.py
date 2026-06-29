import pygame

from code.assets import Assets
from code.settings import CYAN, GREEN, HEIGHT, ORANGE, RED, WHITE, WIDTH, YELLOW


class ResultScreen:
    def __init__(self, window: pygame.Surface, assets: Assets):
        self.window = window
        self.assets = assets
        self.bg = assets.background("ScoreBg.png")
        self.title_font = pygame.font.SysFont("lucidasanstypewriter", 36, bold=True)
        self.font = pygame.font.SysFont("lucidasanstypewriter", 16)

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
            self._center(self.title_font, title, color, HEIGHT // 2 - 42)
            self._center(self.font, subtitle, WHITE, HEIGHT // 2 + 2)
            self._center(self.font, "ENTER - jogar novamente", YELLOW, HEIGHT // 2 + 42)
            self._center(self.font, "ESC - voltar ao menu", CYAN, HEIGHT // 2 + 66)
            pygame.display.flip()

    def _center(self, font: pygame.font.Font, text: str, color: tuple[int, int, int], y: int):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(WIDTH // 2, y))
        self.window.blit(surf, rect)
