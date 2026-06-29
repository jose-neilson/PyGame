import pygame

from code.settings import ASSET_DIR, HEIGHT, WIDTH


class Assets:
    def __init__(self):
        self.images: dict[str, pygame.Surface] = {}
        self.sounds_enabled = True

    def image(self, name: str, scale: int = 1) -> pygame.Surface:
        key = f"{name}:{scale}"
        if key not in self.images:
            path = ASSET_DIR / name
            surface = pygame.image.load(path).convert_alpha()
            if scale != 1:
                size = (surface.get_width() * scale, surface.get_height() * scale)
                surface = pygame.transform.scale(surface, size)
            self.images[key] = surface
        return self.images[key]

    def background(self, name: str) -> pygame.Surface:
        surface = self.image(name)
        if surface.get_size() != (WIDTH, HEIGHT):
            surface = pygame.transform.scale(surface, (WIDTH, HEIGHT))
        return surface

    def play_music(self, name: str, volume: float = 0.35):
        if not self.sounds_enabled:
            return
        try:
            pygame.mixer.music.load(ASSET_DIR / name)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
        except pygame.error:
            self.sounds_enabled = False
