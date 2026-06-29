from pathlib import Path
import sys


if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent
ASSET_DIR = BASE_DIR / "Mountain Shooter Assets" / "asset"

WIDTH = 576
HEIGHT = 324
FPS = 60

TITLE = "Skybound Peaks"
AUTHOR = "Jose Neilson Viana do Nascimento"
RU = "RU: 5176436"

WHITE = (245, 245, 245)
YELLOW = (255, 230, 120)
ORANGE = (255, 150, 60)
GREEN = (70, 210, 120)
CYAN = (90, 220, 230)
RED = (230, 80, 80)
DARK = (24, 31, 38)
PANEL = (15, 24, 31)
PANEL_BORDER = (76, 172, 190)
PLATFORM = (67, 91, 67)
PLATFORM_TOP = (120, 148, 75)

GRAVITY = 0.35
PLAYER_SPEED = 3.0
JUMP_SPEED = -7.2
BULLET_SPEED = 6.0
ENEMY_BULLET_SPEED = 2.6

PLAYER_LIVES = 3
PLAYER_INVULNERABLE_MS = 900
PLAYER_SHOT_COOLDOWN_MS = 260
ENEMY_SHOT_COOLDOWN_MS = 2800
JUMP_BUFFER_MS = 140
COYOTE_TIME_MS = 120

LEVEL_LENGTH = 1650
GOAL_X = 1540
