#Flower tile Game
import pygame
import sys
from os import path
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #initialise game window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title) #What will the window be called?
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "art")
        self.map_data = []
        with open(path.join(game_folder, "map.txt"), "rt") as f:
            for line in f:
                self.map_data.append(line)
        self.player_art = pygame.image.load(path.join(img_folder, "farmer.png")).convert_alpha()

    def new(self):
        #initialise all variables - set self.playing = False to end game
        self.all_sprites = pygame.sprite.Group()
        self.dirt = pygame.sprite.Group()
        self.fence = pygame.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate (tiles):
                if tile == "P":
                    Player(self, col, row)
                if tile == "D":
                    Dirt(self, col, row)
                if tile == "1":
                    Fence(self, col, row)


    def run(self):
        #gameloop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps)/1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        #game loop - update
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, width, tilesize):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, height))
        for y in range(0, height, tilesize):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (width, y))

    def draw(self):
        #game loop - draw
        self.screen.fill(BGCOLOUR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()


    def events(self):
        #game loop - events
        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        #game splash/start screen
        pass

    def show_go_screen(self):
        #gameover/continue screen
        pass

g = Game() #instance of game object
g.show_start_screen()

while True:
    g.new()
    g.run()
    g.show_go_screen()

pygame.quit()
