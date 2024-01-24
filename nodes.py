import pygame
from vector import Vector2
from constants import *


class Node(object):
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.neighbors = {'UP': None, 'DOWN': None, 'LEFT': None, 'RIGHT': None}

    def connect_nodes(self, direction1, other_node):
        self.neighbors[direction1] = other_node
        #other_node.neighbors[direction2] = self

    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, BLUE, line_start, line_end)