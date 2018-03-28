import pygame
import colorsys

#vec = pygame.math.Vector2

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# General
WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Doggo tilemap demo"
BGCOLOR = DARKGREY

# Tiles
TILESIZE = 64
GRIDWITH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player
PLAYER_SPEED = 350
PLAYER_IMG = 'doggo.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)

# HUD
ITEMS_BG = 64