from nodes import NodeGroup
import pygame

def startGame(self):
    self.setBackground()
    self.nodes = NodeGroup()
    self.nodes.setupTestNodes()

def render(self):
    self.screen.blit(self.background, (0,0))
    self.nodes.render(self.screen)
    self.pacman.render(self.screen)
    pygame.display.update()