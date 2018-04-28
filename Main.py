import pygame
import sys
from os import path
from Settings import *
from Sprites import *
from Map import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(200)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(path.realpath('__file__'))

        maps_folder = path.join(game_folder, 'maps')
        images_folder = path.join(game_folder, 'images')
        music_folder = path.join(game_folder, 'music')
        sfx_folder = path.join(game_folder, 'sfx')
        font_folder = path.join(game_folder, 'font')

        self.font = path.join(font_folder, 'GOODDP__.TTF')
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 150))
        self.dim_screen2 = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen2.fill((0, 0, 0, 50))
        self.map = TiledMap(path.join(maps_folder, BOTTOM))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.wallpaper_img = pygame.image.load(path.join(images_folder, WALLPAPER)).convert_alpha()
        self.logo_img = pygame.image.load(path.join(images_folder, LOGO)).convert_alpha()
        self.player_img = pygame.image.load(path.join(images_folder, PLAYER_IMG)).convert_alpha()
        self.doggo_feliz_img = pygame.image.load(path.join(images_folder, DOGGO_FELIZ)).convert_alpha()
        self.doggo_triste_img = pygame.image.load(path.join(images_folder, DOGGO_TRISTE)).convert_alpha()

        self.zanahoria_img = pygame.image.load(path.join(images_folder, ZANAHORIA)).convert_alpha()
        self.tubo_img = pygame.image.load(path.join(images_folder, TUBO)).convert_alpha()
        self.bone_img = pygame.image.load(path.join(images_folder, BONE)).convert_alpha()
        self.santa_img = pygame.image.load(path.join(images_folder, SANTA)).convert_alpha()
        self.gusano_img = pygame.image.load(path.join(images_folder, GUSANO)).convert_alpha()
        self.croco_img = pygame.image.load(path.join(images_folder, CROCO)).convert_alpha()

        self.pause_sfx = pygame.mixer.Sound(path.join(sfx_folder, PAUSE))
        self.pause_sfx.set_volume(.1)
        self.item_sfx = pygame.mixer.Sound(path.join(sfx_folder, ITEMGET))
        self.item_sfx.set_volume(.1)
        self.hit_sfx = pygame.mixer.Sound(path.join(sfx_folder, HIT))
        self.hit_sfx.set_volume(.1)

        self.item_images = {}
        self.paused = False

        self.zanahoria_conseguido = False
        self.tubo_conseguido = False
        self.santa_conseguido = False
        self.croco_conseguido = False
        self.bone_conseguido = False
        self.gusano_conseguido = False

        self.colisionGusano = False
        self.colisionZanahoria = False
        self.colisionTubo = False
        self.colisionSanta = False
        self.colisionCroco = False
        self.colisionBone = False

        self.y = HEIGHT
        self.x = WIDTH

        for item in ITEM_IMAGES:
            self.item_images[item] = pygame.image.load(path.join(images_folder, ITEM_IMAGES[item]))

        pygame.mixer.music.load(path.join(music_folder, FIRST_LEVEL))

        self.steps_sounds = []
        for sfx in STEPS:
            my_sfx = pygame.mixer.Sound(path.join(sfx_folder, sfx))
            my_sfx.set_volume(.02)
            self.steps_sounds.append(my_sfx)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'Wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'Zanahoria':
                Item(self, obj_center, tile_object.name)
            if tile_object.name == 'Bone':
                Item(self, obj_center, tile_object.name)
            if tile_object.name == 'Croco':
                Item(self, obj_center, tile_object.name)
            if tile_object.name == 'Gusano':
                Item(self, obj_center, tile_object.name)
            if tile_object.name == 'Tubo':
                Item(self, obj_center, tile_object.name)
            if tile_object.name == 'Santa':
                Item(self, obj_center, tile_object.name)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        pygame.mixer.music.play(loops = -1)
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
                pygame.mixer.music.set_volume(.25)
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

        hits = pygame.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'Gusano':
                #print(hit.type)
                self.colisionGusano = True
                if self.gusano_conseguido:
                    self.item_sfx.play()
                    hit.kill()

            if hit.type == 'Zanahoria':
                #print(hit.type)
                self.colisionZanahoria = True
                if self.zanahoria_conseguido:
                    self.item_sfx.play()
                    hit.kill()

            if hit.type == 'Tubo':
                #print(hit.type)
                self.colisionTubo = True
                if self.tubo_conseguido:
                    self.item_sfx.play()
                    hit.kill()

            if hit.type == 'Santa':
                #print(hit.type)
                self.colisionSanta = True
                if self.santa_conseguido:
                    self.item_sfx.play()
                    hit.kill()

            if hit.type == 'Croco':
                #print(hit.type)
                self.colisionCroco = True
                if self.croco_conseguido:
                    self.item_sfx.play()
                    hit.kill()

            if hit.type == 'Bone':
                #print(hit.type)
                self.colisionBone = True
                if self.bone_conseguido:
                    self.item_sfx.play()
                    hit.kill()

        #print(self.player.hit_rect.center)

    def draw_gui(self, x, y):
        outline_rect = pygame.Rect(x, y, ITEMS_BG, ITEMS_BG)
        pygame.draw.rect(self.screen, BLACK, outline_rect)
        pygame.draw.rect(self.screen, WHITE, outline_rect, 2)

    def draw_text(self, text, font_name, size, color, x, y, align):
        font = pygame.font.Font(font_name, size)
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

        self.draw_text("Consigue todos los juguetes!", self.font, 50, BLACK, 1052, 682, align = "center")
        self.draw_text("Consigue todos los juguetes!", self.font, 50, WHITE, 1050, 680, align = "center")

        for i in range(10, 500, 75):
            self.draw_gui(i, 10)

        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Pausa", self.font, 175, WHITE, WIDTH / 2, 100, align = "center")
            self.draw_text("Controles:", self.font, 75, WHITE, WIDTH / 2, 300, align = "center")
            self.draw_text("Flechas para moverse", self.font, 50, WHITE, WIDTH / 2, 400, align = "center")
            self.draw_text("P = Pausar", self.font, 50, WHITE, WIDTH / 2, 450, align = "center")
            self.draw_text("Z = Interactuar", self.font, 50, WHITE, WIDTH / 2, 500, align = "center")
            self.draw_text("ESC = Salir del juego", self.font, 50, WHITE, WIDTH / 2, 550, align = "center")

        if self.zanahoria_conseguido:
            self.screen.blit(self.zanahoria_img, (20, 10))
        if self.gusano_conseguido:
            self.screen.blit(self.gusano_img, (95, 10))
        if self.tubo_conseguido:
            self.screen.blit(self.tubo_img, (160, 20))
        if self.bone_conseguido:
            self.screen.blit(self.bone_img, (235, 30))
        if self.santa_conseguido:
            self.screen.blit(self.santa_img, (320, 10))
        if self.croco_conseguido:
            self.screen.blit(self.croco_img, (385, 30))

        if self.zanahoria_conseguido and self.gusano_conseguido and self.tubo_conseguido and self.bone_conseguido and self.santa_conseguido and self.croco_conseguido:
            self.show_go_screen()

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                if event.key == pygame.K_p:
                    self.paused = not self.paused
                    self.pause_sfx.play()
                    pygame.mixer.music.set_volume(.1)

                if event.key == pygame.K_z and self.colisionGusano:
                    self.gusano_conseguido = True

                if event.key == pygame.K_z and self.colisionZanahoria:
                    self.zanahoria_conseguido = True

                if event.key == pygame.K_z and self.colisionTubo:
                    self.tubo_conseguido = True

                if event.key == pygame.K_z and self.colisionSanta:
                    self.santa_conseguido = True

                if event.key == pygame.K_z and self.colisionCroco:
                    self.croco_conseguido = True

                if event.key == pygame.K_z and self.colisionBone:
                    self.bone_conseguido = True

    def show_start_screen(self):
        self.y -= 10
        if self.y == -720:
            self.y = 720

        self.screen.blit(self.wallpaper_img, (0, 0))
        self.screen.blit(self.dim_screen2, (0, 0))
        self.screen.blit(self.logo_img, (0, 128))
        self.screen.blit(self.doggo_feliz_img, (850, self.y))
        self.draw_text("Controles:", self.font, 75, BLACK, (WIDTH / 2) + 5, 230, align = "center")
        self.draw_text("Flechas para moverse", self.font, 50, BLACK, (WIDTH / 2) + 5, 280, align = "center")
        self.draw_text("P = Pausar", self.font, 50, BLACK, (WIDTH / 2) + 5, 355, align = "center")
        self.draw_text("Z = Interactuar", self.font, 50, BLACK, (WIDTH / 2) + 5, 405, align = "center")
        self.draw_text("ESC = Salir del juego", self.font, 50, BLACK, (WIDTH / 2) + 5, 455, align = "center")
        self.draw_text("Presiona 'Z' para empezar", self.font, 25, BLACK, (WIDTH / 2) + 3, 653, align = "center")

        self.draw_text("Controles:", self.font, 75, WHITE, WIDTH / 2, 225, align = "center")
        self.draw_text("Flechas para moverse", self.font, 50, WHITE, WIDTH / 2, 275, align = "center")
        self.draw_text("P = Pausar", self.font, 50, WHITE, WIDTH / 2, 350, align = "center")
        self.draw_text("Z = Interactuar", self.font, 50, WHITE, WIDTH / 2, 400, align = "center")
        self.draw_text("ESC = Salir del juego", self.font, 50, WHITE, WIDTH / 2, 450, align = "center")
        self.draw_text("Presiona 'Z' para empezar", self.font, 25, WHITE, WIDTH / 2, 650, align = "center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_z:
                    pygame.mixer.music.stop()
                    game.run()
        pygame.display.flip()

    def show_go_screen(self):
        self.screen.blit(self.wallpaper_img, (0, 0))
        self.screen.blit(self.dim_screen2, (0, 0))
        self.screen.blit(self.logo_img, (0, 128))
        self.screen.blit(self.doggo_feliz_img, (850, 0))
        self.draw_text("¡Gracias por jugar!", self.font, 75, BLACK, (WIDTH / 2) + 5, 230, align = "center")
        self.draw_text("Presiona ESC para salir", self.font, 50, BLACK, (WIDTH / 2) + 5, 455, align = "center")

        self.draw_text("¡Gracias por jugar!", self.font, 75, WHITE, WIDTH / 2, 225, align = "center")
        self.draw_text("Presiona ESC para salir", self.font, 50, WHITE, WIDTH / 2, 450, align = "center")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
        pygame.display.flip()

game = Game()

while True:
    game.new()
    game.show_start_screen()