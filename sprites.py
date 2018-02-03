import pygame
from settings import *
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_art
        self.image.set_colorkey(BLACK) #make black transparent
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collision(dx, dy):
            self.x += dx
            self.y += dy


    def keypress(self):
        dist = 1
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            #self.y += 1
            self.move(dy = dist)
        elif key[pygame.K_UP]:
            #self.y -= 1
            self.move(dy = -dist)
        elif key[pygame.K_RIGHT]:
            #self.x += 1
            self.move(dx = dist)
        elif key[pygame.K_LEFT]:
            #self.x -= 1
            self.move(dx = -dist)


    def collision(self, dx=0, dy=0):
        for fence in self.game.fence:
            if fence.x == self.x + dx and fence.y == self.y + dy:
                return True
        if self.x + dx <= 0 or self.x + dx >= width:
                return True
        if self.y + dy <= 0 or self.y + dy >= height:
                return True
        return False

    def update(self):
        self.keypress()
        self.rect.x = self.x * tilesize
        self.rect.y =  self.y * tilesize

class Dirt(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.dirt
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tilesize
        self.rect.y = y * tilesize

class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load(os.path.join(img_folder, "grass.png")).convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tilesize
        self.rect.y = y * tilesize

class Fence(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fence
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tilesize
        self.rect.y = y * tilesize
