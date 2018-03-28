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

        self.map = Map(path.join(maps_folder, 'Map1.txt'))
        self.player_img = pygame.image.load(path.join(images_folder, PLAYER_IMG)).convert_alpha()

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_player_health(surf, x, y):
        outline_rect = pygame.Rect(x, y, ITEMS_BG, ITEMS_BG)
        outline_outline_rect = pygame.Rect(x, y, ITEMS_BG, ITEMS_BG)
        pygame.draw.rect(surf, BLACK, outline_rect)
        pygame.draw.rect(surf, WHITE, outline_outline_rect, 2)

    def draw(self):
        pygame.display.set_caption("{:-2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for i in range(10, 500, 75):
            self.draw_player_health(self.screen, i, 10)
            self.draw_player_health(self.screen, i, 10)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

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