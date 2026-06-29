import pygame

from code.assets import Assets
from code.entities import Bullet, Enemy, Player
from code.settings import (
    CYAN,
    DARK,
    GOAL_X,
    GREEN,
    HEIGHT,
    LEVEL_LENGTH,
    PLATFORM,
    PLATFORM_TOP,
    RED,
    WHITE,
    WIDTH,
    YELLOW,
)


class Level:
    def __init__(self, window: pygame.Surface, assets: Assets, number: int = 1):
        self.window = window
        self.assets = assets
        self.number = number
        bg_count = 7 if number == 1 else 5
        self.bg_layers = [assets.background(f"Level{number}Bg{i}.png") for i in range(bg_count)]
        self.font = pygame.font.SysFont("lucidasanstypewriter", 13)
        self.platforms = self._platforms()
        self.player = Player(assets.image("Player1.png"), assets.image("Player1Shot.png", 2))
        self.bullets: list[Bullet] = []
        self.enemies = self._enemies()
        self.camera_x = 0

    def run(self) -> str:
        self.assets.play_music(f"Level{self.number}.mp3", 0.35)
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60)
            now = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "menu"
                    if event.key == pygame.K_SPACE:
                        self.player.request_jump(now)
                    if event.key in (pygame.K_j, pygame.K_RCTRL, pygame.K_LCTRL):
                        bullet = self.player.shoot(now)
                        if bullet:
                            self.bullets.append(bullet)

            keys = pygame.key.get_pressed()
            dx = self.player.handle_input(keys)
            self.player.update(self.platforms, dx, now)

            for enemy in self.enemies:
                enemy.update()
                bullet = enemy.shoot(now, self.player)
                if bullet:
                    self.bullets.append(bullet)

            for bullet in self.bullets:
                bullet.update()

            self._collisions(now)
            self.enemies = [enemy for enemy in self.enemies if enemy.alive]
            self.bullets = [bullet for bullet in self.bullets if bullet.alive]

            self.camera_x = max(0, min(self.player.rect.centerx - WIDTH // 2, LEVEL_LENGTH - WIDTH))
            self._draw(dt)

            if self.player.lives <= 0 or self.player.rect.top > HEIGHT + 80:
                return "lose"
            if self.player.rect.centerx >= GOAL_X and not self.enemies:
                return "level2" if self.number == 1 else "win"

    def _platforms(self) -> list[pygame.Rect]:
        if self.number == 2:
            return [
                pygame.Rect(0, 286, 300, 38),
                pygame.Rect(360, 248, 145, 24),
                pygame.Rect(565, 214, 120, 24),
                pygame.Rect(760, 178, 140, 24),
                pygame.Rect(980, 226, 150, 24),
                pygame.Rect(1210, 258, 150, 24),
                pygame.Rect(1430, 286, 220, 38),
            ]
        return [
            pygame.Rect(0, 286, 360, 38),
            pygame.Rect(415, 252, 190, 24),
            pygame.Rect(665, 218, 170, 24),
            pygame.Rect(900, 258, 210, 24),
            pygame.Rect(1180, 222, 160, 24),
            pygame.Rect(1420, 286, 230, 38),
        ]

    def _enemies(self) -> list[Enemy]:
        enemy1 = self.assets.image("Enemy1.png")
        enemy2 = self.assets.image("Enemy2.png")
        shot1 = self.assets.image("Enemy1Shot.png", 2)
        shot2 = self.assets.image("Enemy2Shot.png", 3)
        if self.number == 2:
            return [
                Enemy(430, 248, enemy1, shot1, 365, 505, health=2, speed=1),
                Enemy(625, 214, enemy1, shot1, 570, 685, health=2, speed=1),
                Enemy(825, 178, enemy2, shot2, 765, 900, health=4, speed=1),
                Enemy(1050, 226, enemy1, shot1, 985, 1130, health=2, speed=1),
                Enemy(1285, 258, enemy2, shot2, 1215, 1360, health=8, speed=1),
            ]
        return [
            Enemy(520, 252, enemy1, shot1, 420, 600, health=2, speed=1),
            Enemy(760, 218, enemy1, shot1, 670, 835, health=2, speed=1),
            Enemy(1010, 258, enemy1, shot1, 905, 1110, health=2, speed=1),
            Enemy(1260, 222, enemy2, shot2, 1185, 1340, health=6, speed=1),
        ]

    def _collisions(self, now: int):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.hurt(now)

        for bullet in self.bullets:
            if bullet.owner == "player":
                for enemy in self.enemies:
                    if enemy.alive and bullet.rect.colliderect(enemy.rect):
                        enemy.hit()
                        bullet.alive = False
                        if not enemy.alive:
                            self.player.score += 100
                        break
            elif bullet.rect.colliderect(self.player.rect):
                self.player.hurt(now)
                bullet.alive = False

    def _draw(self, dt: int):
        self._draw_background()
        self._draw_platforms()
        self._draw_goal()
        for bullet in self.bullets:
            bullet.draw(self.window, self.camera_x)
        for enemy in self.enemies:
            enemy.draw(self.window, self.camera_x)
        self.player.draw(self.window, self.camera_x)
        self._draw_hud(dt)
        pygame.display.flip()

    def _draw_background(self):
        self.window.blit(self.bg_layers[0], (0, 0))
        for index, layer in enumerate(self.bg_layers[1:], start=1):
            parallax = (self.camera_x * index * 0.08) % WIDTH
            self.window.blit(layer, (-parallax, 0))
            self.window.blit(layer, (WIDTH - parallax, 0))

    def _draw_platforms(self):
        for platform in self.platforms:
            rect = platform.move(-self.camera_x, 0)
            pygame.draw.rect(self.window, PLATFORM, rect)
            pygame.draw.rect(self.window, PLATFORM_TOP, (rect.x, rect.y, rect.w, 4))

    def _draw_goal(self):
        x = GOAL_X - self.camera_x
        pygame.draw.rect(self.window, DARK, (x - 5, 188, 10, 98))
        pygame.draw.rect(self.window, WHITE, (x - 2, 188, 4, 98))
        pygame.draw.polygon(self.window, YELLOW, [(x + 3, 190), (x + 70, 210), (x + 3, 232)])
        pygame.draw.circle(self.window, YELLOW, (x, 184), 7)
        label = "BANDEIRA"
        if self.enemies and abs(self.player.rect.centerx - GOAL_X) < 160:
            label = "DERROTE TODOS"
        surf = self.font.render(label, True, YELLOW)
        self.window.blit(surf, (x - 46, 170))

    def _draw_hud(self, dt: int):
        fps = 1000 / dt if dt else 0
        texts = [
            (f"Fase: {self.number}", YELLOW, 8, 8),
            (f"Vidas: {self.player.lives}", RED, 8, 24),
            (f"Pontos: {self.player.score}", GREEN, 8, 40),
            (f"Inimigos: {len(self.enemies)}", CYAN, 8, 56),
            (f"FPS: {fps:.0f}", WHITE, WIDTH - 74, 8),
        ]
        for text, color, x, y in texts:
            surf = self.font.render(text, True, color)
            self.window.blit(surf, (x, y))
