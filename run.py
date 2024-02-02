import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from ghosts import GhostGroup
#from pellets import PelletGroup
#from sprites import *
#from text import TextGroup
#from mazedata import MazeData


class GameController(object):
    def __init__(self):
        self.ghosts = None
        self.pellets = None
        self.nodes = None
        self.pacman = None
        self.mazesprites = None
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.background_norm = None
        self.background_flash = None
        self.level = 0
        self.lives = 5
        self.score = 0
        self.textgroup = TextGroup()
        self.lifesprites = LifeSprites(self.lives)
        self.flashBG = False
        self.flashTime = 0.2
        self.flashTimer = 0
        self.mazedata = MazeData()

    def setBackground(self):
        self.background_norm = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
        self.background_flash = pygame.surface.Surface(SCREENSIZE).convert()
        self.background_flash.fill(BLACK)
        self.background_norm = self.mazesprites.constructBackground(self.background_norm, self.level % 5)
        self.background_flash = self.mazesprites.constructBackground(self.background_flash, 5)
        self.flashBG = False
        set.background = self.background_norm

    def startGame(self):
        self.mazedata.loadMaze(self.level)
        #self.mazesprites = MazeSprites(self.mazedata.obj.name + ".txt", self.mazedata.obj.name + "_rotation.txt")
        self.setBackground()
        self.nodes = NodeGroup(self.mazedata.obj.name + ".txt")
        self.mazedata.obj.setPortalPairs(self.nodes)
        self.mazedata.obj.connectHomeNodes(self.nodes)
        self.pacman = Pacman(self.nodes.getNodeFromTiles(*self.mazedata.obj.pacmanStart))
        #self.pellets = PelletGroup(self.mazedata.obj.name + ".txt")
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)

        self.ghosts.pinky.setColor(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 3)))
        self.ghosts.inky.setColor(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(0, 3)))
        self.ghosts.clyde.setColor(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(4, 3)))
        self.ghosts.blinky.setColor(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 0)))
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 0)))

        self.nodes.denyHomeAccess(self.pacman)
        self.nodes.denyHomeAccessList(self.ghosts)
        self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
        self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.inky)
        self.mazedata.obj.denyGhostsAccess(self.ghosts, self.nodes)

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
