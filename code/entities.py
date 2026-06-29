from __future__ import annotations

import pygame

from code.settings import (
    BULLET_SPEED,
    ENEMY_BULLET_SPEED,
    ENEMY_SHOT_COOLDOWN_MS,
    GRAVITY,
    HEIGHT,
    JUMP_SPEED,
    JUMP_BUFFER_MS,
    LEVEL_LENGTH,
    COYOTE_TIME_MS,
    PLAYER_INVULNERABLE_MS,
    PLAYER_LIVES,
    PLAYER_SHOT_COOLDOWN_MS,
    PLAYER_SPEED,
)


class Bullet:
    def __init__(self, x: int, y: int, direction: int, image: pygame.Surface, owner: str):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.owner = owner
        self.speed = BULLET_SPEED if owner == "player" else ENEMY_BULLET_SPEED
        self.alive = True

    def update(self):
        self.rect.x += int(self.speed * self.direction)
        if self.rect.right < -80 or self.rect.left > LEVEL_LENGTH + 80:
            self.alive = False

    def draw(self, surface: pygame.Surface, camera_x: int):
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y))


class Player:
    def __init__(self, image: pygame.Surface, shot_image: pygame.Surface):
        self.image = image
        self.shot_image = shot_image
        self.rect = self.image.get_rect(topleft=(40, 190))
        self.vel_y = 0.0
        self.facing = 1
        self.on_ground = False
        self.lives = PLAYER_LIVES
        self.score = 0
        self.last_hit = -PLAYER_INVULNERABLE_MS
        self.last_shot = -PLAYER_SHOT_COOLDOWN_MS
        self.last_jump_pressed = -JUMP_BUFFER_MS
        self.last_on_ground = 0

    def handle_input(self, keys: pygame.key.ScancodeWrapper):
        dx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= PLAYER_SPEED
            self.facing = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += PLAYER_SPEED
            self.facing = 1
        return dx

    def request_jump(self, now: int):
        self.last_jump_pressed = now

    def jump(self, now: int):
        jump_buffered = now - self.last_jump_pressed <= JUMP_BUFFER_MS
        recently_grounded = now - self.last_on_ground <= COYOTE_TIME_MS
        if jump_buffered and (self.on_ground or recently_grounded):
            self.vel_y = JUMP_SPEED
            self.on_ground = False
            self.last_jump_pressed = -JUMP_BUFFER_MS

    def shoot(self, now: int) -> Bullet | None:
        if now - self.last_shot < PLAYER_SHOT_COOLDOWN_MS:
            return None
        self.last_shot = now
        x = self.rect.right if self.facing > 0 else self.rect.left
        return Bullet(x, self.rect.centery, self.facing, self.shot_image, "player")

    def update(self, platforms: list[pygame.Rect], dx: float, now: int):
        self.rect.x += int(dx)
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(LEVEL_LENGTH, self.rect.right)

        self.vel_y += GRAVITY
        self.vel_y = min(self.vel_y, 8)
        self.rect.y += int(self.vel_y)
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y >= 0 and self.rect.bottom - int(self.vel_y) <= platform.top + 4:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.last_on_ground = now
                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0

        self.jump(now)

    def hurt(self, now: int):
        if now - self.last_hit < PLAYER_INVULNERABLE_MS:
            return
        self.last_hit = now
        self.lives -= 1
        self.vel_y = -4

    def draw(self, surface: pygame.Surface, camera_x: int):
        if pygame.time.get_ticks() - self.last_hit < PLAYER_INVULNERABLE_MS:
            if (pygame.time.get_ticks() // 100) % 2 == 0:
                return
        image = self.image if self.facing > 0 else pygame.transform.flip(self.image, True, False)
        surface.blit(image, (self.rect.x - camera_x, self.rect.y))


class Enemy:
    def __init__(
        self,
        x: int,
        y: int,
        image: pygame.Surface,
        shot_image: pygame.Surface,
        left_limit: int,
        right_limit: int,
        health: int,
        speed: int = 1,
    ):
        self.image = image
        self.shot_image = shot_image
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.direction = -1
        self.speed = speed
        self.health = health
        self.last_shot = pygame.time.get_ticks()
        self.alive = True

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left <= self.left_limit:
            self.rect.left = self.left_limit
            self.direction = 1
        if self.rect.right >= self.right_limit:
            self.rect.right = self.right_limit
            self.direction = -1

    def shoot(self, now: int, player: Player) -> Bullet | None:
        if abs(player.rect.centerx - self.rect.centerx) > 360:
            return None
        if now - self.last_shot < ENEMY_SHOT_COOLDOWN_MS:
            return None
        self.last_shot = now
        direction = -1 if player.rect.centerx < self.rect.centerx else 1
        return Bullet(self.rect.centerx, self.rect.centery, direction, self.shot_image, "enemy")

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False

    def draw(self, surface: pygame.Surface, camera_x: int):
        image = self.image if self.direction < 0 else pygame.transform.flip(self.image, True, False)
        surface.blit(image, (self.rect.x - camera_x, self.rect.y))
