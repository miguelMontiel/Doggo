import pygame
from random import uniform
from settings import *
from tilemap import collide_hit_rect
from random import choice, random

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center

        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH

    def collide_with_walls(sprite, group, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centerx > sprite.hit_rect.centerx:
                    sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2

                if hits[0].rect.centerx < sprite.hit_rect.centerx:
                    sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2

                sprite.vel.x = 0
                sprite.hit_rect.centerx = sprite.pos.x

        if dir == 'y':
            hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centery > sprite.hit_rect.centery:
                    sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2

                if hits[0].rect.centery < sprite.hit_rect.centery:
                    sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2

                sprite.vel.y = 0
                sprite.hit_rect.centery = sprite.pos.y

    def playerSFX(self):
        if random() < 0.4:
            choice(self.game.steps_sounds).play()

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vel = vec(-PLAYER_SPEED, 0)
            self.image = pygame.transform.flip(self.game.player_img, True, False)
            self.playerSFX()

        if keys[pygame.K_RIGHT]:
            self.vel = vec(PLAYER_SPEED, 0)
            self.image = pygame.transform.flip(self.game.player_img, False, False)
            self.playerSFX()

        if keys[pygame.K_UP]:
            self.vel = vec(0, -PLAYER_SPEED)
            self.playerSFX()

        if keys[pygame.K_DOWN]:
            self.vel = vec(0, PLAYER_SPEED)
            self.playerSFX()

        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.vel = vec(-PLAYER_SPEED, PLAYER_SPEED)
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.vel = vec(PLAYER_SPEED, PLAYER_SPEED)
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.vel = vec(-PLAYER_SPEED, -PLAYER_SPEED)
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.vel = vec(PLAYER_SPEED, -PLAYER_SPEED)

    def update(self):
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls(self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls(self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y