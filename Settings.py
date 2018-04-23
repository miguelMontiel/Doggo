import pygame
import colorsys

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# General
LOGO = "logoR.png"
WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Doggo tilemap demo"
BGCOLOR = DARKGREY
BOTTOM = "Bottom.tmx"
TOP = "Top.tmx"

# Tiles
TILESIZE = 64
GRIDWITH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player
PLAYER_SPEED = 350
PLAYER_IMG = 'doggo.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)

# Items
ITEM_IMAGES = {'Zanahoria': 'Zanahoria.png',
               'Bone': 'Bone.png',
               'Croco': 'Croco.png',
               'Santa': 'Santa.png',
               'Tubo': 'Tubo.png',
               'Gusano': 'Gusano.png'}

# HUD
ITEMS_BG = 64
BUBBLE_HEIGHT = 240
BUBBLE_WIDTH = 1024

# Music
MAIN_MENU = 'Bobber_Loop.wav'
FIRST_LEVEL = 'Patakas_World.wav'
SECOND_LEVEL = 'My_Little_Adventure.mp3'

# SFX
STEPS = ['Step1.wav', 'Step2.wav', 'Step3.wav']