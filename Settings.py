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
WALLPAPER = "wallpaper.jpg"
LOGO = "logoR.png"
WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Doggo tilemap demo"
BGCOLOR = DARKGREY
BOTTOM = "Bottom.tmx"

# Tiles
TILESIZE = 64
GRIDWITH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player
PLAYER_SPEED = 350
PLAYER_IMG = 'doggo.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)

# Doggo
DOGGO_FELIZ = 'DoggoFeliz720.png'
DOGGO_TRISTE = 'DoggoTriste720.png'

# Items
ITEM_IMAGES = {'Zanahoria': 'Zanahoria.png',
               'Bone': 'Bone.png',
               'Croco': 'Croco.png',
               'Santa': 'Santa.png',
               'Tubo': 'Tubo.png',
               'Gusano': 'Gusano.png'}

ZANAHORIA = 'Zanahoria.png'
BONE = 'Bone.png'
CROCO = 'Croco.png'
SANTA = 'Santa.png'
TUBO = 'Tubo.png'
GUSANO = 'Gusano.png'

# HUD
ITEMS_BG = 64
BUBBLE_HEIGHT = 240
BUBBLE_WIDTH = 1024

# Music
MAIN_MENU = 'My_Little_Adventure.mp3'
FIRST_LEVEL = 'Patakas_World.wav'
END_MENU = 'Bobber_Loop.wav'

# SFX
STEPS = ['Step1.wav', 'Step2.wav', 'Step3.wav']
HIT = 'Hit.wav'
ITEMGET = 'ItemGet.wav'
PAUSE = 'Pause.wav'
