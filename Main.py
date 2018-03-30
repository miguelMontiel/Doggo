import pygame
import sys
from os import path
from Settings import *
from Sprites import *
from Maps import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(200)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        maps_folder = path.join(game_folder, 'maps')
        images_folder = path.join(game_folder, 'images')
        music_folder = path.join(game_folder, 'music')
        sfx_folder = path.join(game_folder, 'sfx')
        font_folder = path.join(game_folder, 'font')

        self.font = path.join(font_folder, 'GOODDP__.TTF')
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 150))
        self.map = TiledMap(path.join(maps_folder, 'Bottom.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pygame.image.load(path.join(images_folder, PLAYER_IMG)).convert_alpha()
        self.paused = False

        pygame.mixer.music.load(path.join(music_folder, FIRST_LEVEL))

        self.steps_sounds = []
        for sfx in STEPS:
            my_sfx = pygame.mixer.Sound(path.join(sfx_folder, sfx))
            my_sfx.set_volume(.05)
            self.steps_sounds.append(my_sfx)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'Wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        pygame.mixer.music.play(loops = -1)
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
                pygame.mixer.music.set_volume(.5)
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_player_health(surf, x, y):
        outline_rect = pygame.Rect(x, y, ITEMS_BG, ITEMS_BG)
        outline_outline_rect = pygame.Rect(x, y, ITEMS_BG, ITEMS_BG)
        pygame.draw.rect(surf, BLACK, outline_rect)
        pygame.draw.rect(surf, WHITE, outline_outline_rect, 2)

    def draw_text(self, text, font_name, size, color, x, y, align = "nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        pygame.display.set_caption("{:-2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        #for i in range(10, 500, 75):
            #self.draw_player_health(self.screen, 10, 10)

        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Pausa", self.font, 125, WHITE, WIDTH / 2, HEIGHT / 2, align = "center")

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused
                    pygame.mixer.music.set_volume(.1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

game = Game()
game.show_start_screen()

while True:
    game.new()
    game.run()
    game.show_go_screen()