import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from ghosts import GhostGroup


class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup("carte2.txt")
        self.pacman = Pacman(self.nodes.getStartTempNode())
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.ghosts.update(dt)
        self.checkEvents()
        self.render()

    def checkPelletEvents(self):
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.pelletList.remove(pellet)
            if pellet.name is POWERPELLET:
                self.ghosts.startFreight()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        self.ghosts.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()