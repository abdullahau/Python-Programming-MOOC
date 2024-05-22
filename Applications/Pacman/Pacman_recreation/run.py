import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup


class GameController(object):
    # Instantiation of the class
    def __init__(self):
        # Pygame initialization
        pygame.init()
        # Set Screen size
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
    
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        # Set background color as `black` from `constants`
        self.background.fill(BLACK)
    
    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.nodes.setupTestNodes()
        self.pacman = Pacman()


    def update(self):
        # returns the amount of time that has passed since the last time this line was called
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.checkEvents()
        self.render()    


    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()    
        

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()